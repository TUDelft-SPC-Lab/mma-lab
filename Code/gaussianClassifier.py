"""
Simple Gaussian Classifier for Music Genre Classification Lab
EAAAI - 2012
Note: This code is not optimized for performance. Rather
      it was developed to be explicit so that it 
      can be ported to other programming languages.

Author: Douglas Turnbull, EAAI 2012 Model AI Assignment, Feb 2012
License: CC Attribution 3.0 https://creativecommons.org/licenses/by/3.0/us/
Modifications by Mark Pasterkamp and Sokratis Kariotis
"""
from os import listdir   
from numpy import array, mean, cov, append, linalg, tile, dot, transpose, zeros, argmin, sum, median
from random import shuffle
import sys

# classifies music my genre 
# returns confusion matrix and classification accuracy for randomly partitioned data
def classifyMusic(genres, data, trainingFactor):

    dSize = len(data[0])
    rIdx = range(dSize)
    shuffle(rIdx)
    trainIdx = rIdx[0:int(dSize*trainingFactor)]
    testIdx  = rIdx[int(dSize*trainingFactor):]
    
    gModel= list()
    for g in range(len(genres)):
      trainMat = data[g][trainIdx[0]]['featureMat']
      for i in range(1,len(trainIdx)):
        trainMat = append(trainMat, data[g][trainIdx[i]]['featureMat'], axis =0)
      gModel.append({'mean':mean(trainMat,0), 'cov':cov(trainMat,rowvar=0),\
                    'icov':linalg.inv(cov(trainMat,rowvar=0))})
    
    meanUNLL = zeros((len(genres),len(testIdx),len(genres)))
    guess = zeros((len(genres),len(testIdx)))
    for gs in range(len(genres)):
      for t in range(len(testIdx)):
        ts = testIdx[t]
        x = data[gs][ts]['featureMat']
        [r, c] =x.shape               
        for m in range(len(genres)):
          unll = zeros((r,1))
          
          for v in range(r):
            diff = (x[v] - gModel[m]['mean'])
            res = dot(diff, gModel[m]['icov'])
            res = dot(res, transpose(diff))
            unll[v] = res         

          meanUNLL[gs][t][m] = mean(unll)
        guess[gs][t] = argmin(meanUNLL[gs][t])

    [cfm, acc] = createConfusionMatrix(guess)
    print "Trial Accuracy = ", acc
    return cfm, acc     
    
# loads metadata (song & artist name) and audio feature vectors for all songs
# format:
#    # Count On Me - Bruno Mars
#    0.0,171.13,9.469,-28.48,57.491,-50.067,14.833,5.359,-27.228,0.973,-10.64,-7.228
    #    29.775,-90.263,-47.86,14.023,13.797,189.87,50.924,-31.823,-45.63,104.501,82.114,-13.67
#
# returns data in for of "list of lists of dict" where 
#   first index is the genre and the second index corresponds to a song
#   dict contains 'song', 'artist' , and 'featureMat'
    
def loadData(dataDir, genres):    
    data = list()
    for g in range(len(genres)):
      genreDir = dataDir+"/"+genres[g]
      data.append(list())
      sFiles = listdir(genreDir)
      for s in range(len(sFiles)):
        
        sFile = genreDir+"/"+sFiles[s]
        f = open(sFile)
        lines = f.readlines()
        meta = lines[0].replace("#","").split("-")
        songDict = {'file':sFiles[s],'song': meta[0].strip(), 'artist':meta[1].strip()}
        
        mat = list()
        for i in range(1,len(lines)):
          vec = lines[i].split(",")
          for j in range(len(vec)):
            vec[j] = float(vec[j])
          mat.append(vec)  
              
        songDict['featureMat'] = array(mat)  
        data[g].append(songDict)
    
    return data 
      
def createConfusionMatrix(resultMat):
    [rows, cols] = resultMat.shape
    confMat = zeros((rows,rows))
    acc = 0
    for r in range(rows):
      for c in range(cols):
        confMat[resultMat[r][c]][r] += 1
        if resultMat[r][c] == r:
          acc += 1
    return confMat, float(acc)/(rows*cols)
 
def randomFoldCrossValidation(numTrials = 10, trainingFactor = 0.8):
    dataDir = "Music_Features"
    genres = ['classical','country','jazz','pop','rock','techno']
    
    print "Loading Data..."
    data = loadData(dataDir, genres)
    [cfm, acc] = classifyMusic(genres,data, trainingFactor)
    for i in range(numTrials-1):
      newCfm, newAcc = classifyMusic(genres,data, trainingFactor)
      cfm = cfm + newCfm
      acc = acc + newAcc
  
    print genres
    print
    printConfusionMatrix(cfm)
    print "\nOverall Accuracy:",acc/float(numTrials)

def printConfusionMatrix(cfm):
    genres = ['clas', 'coun', 'jazz', 'pop', 'rock', 'tech']
    spacing = 8
    mat = []
    
    firstRow = [' ' * (spacing)] + genres + ['total']
    mat.append(firstRow)
    
    sumRows = sum(cfm, axis = 1)
    sumCols = sum(cfm, axis = 0)
    
    for i in range(len(cfm)):
        row = [genres[i]] + cfm[i].tolist() + [sumRows[i]]
        mat.append(row)
    
    lastRow = ['total']
    for i in sumCols:
        lastRow.append(i)
    mat.append(lastRow)

    print('\n'.join([''.join([('{:'+ str(spacing - 2) + '}').\
        format(item) for item in row]) for row in mat]))

# main program
if len(sys.argv) > 1:
    randomFoldCrossValidation(10, float(sys.argv[1]))
else:
    randomFoldCrossValidation(10)    
