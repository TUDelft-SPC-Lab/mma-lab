README file on the audio-visual speech data for HW#4
  -Stephen Chu, 3/3/2002

The files are named in the following way

  [m].[n].[a|v].fea

where
  [m] is the class label.  In this case, we are considering a isolated digit
      recognition task,  with only two digits: "2" and "5".
  [n] is the index of the example.   You'll need this to know the correspon-
      dence between the audio and the visual features.  There are a total of
      10 examples.
  [a|v] "a" indicates audio feature, and "v" indicates visual feature.   The 
      audio features are 24-dimensional MFCCs. The visual features has three
      compnents, [w, h1, h2].   w is the distance between the mouth corners;
      h1 and h2 measure the distances  between the upper/lower lips  and the 
      line connecting the mouth corners. 

