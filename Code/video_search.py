import pickle
import numpy as np
from pysqlite2 import dbapi2 as sqlite
from os.path import basename

class Searcher:

    def __init__(self, db):
        self.con = sqlite.connect(db)

	def __del__(self):
		self.con.close()
     
	def get_filename(self,vidid):
		""" Return the filename for a video id"""
		s = self.con.execute("select filename from vidlist where rowid='%d'" % vidid).fetchone()
		return s[0]

    def get_colorhists_for(self, vid_name):
        return self.get_features_for(vid_name, "colorhists")

    def get_temporaldiffs_for(self, vid_name):
        return self.get_features_for(vid_name, "tempdiffs")

    def get_audiopowers_for(self, vid_name):
        return self.get_features_for(vid_name, "audiopowers")

    def get_mfccs_for(self, vid_name):
        return self.get_features_for(vid_name, "mfccs")

    def get_chdiffs_for(self, vid_name):
        return self.get_features_for(vid_name, "chdiffs")

    def get_features_for(self, vid_name, feature):
        vidid = self.con.execute("select rowid from vidlist where filename='%s'" % basename(vid_name)).fetchone()
        query = "select features from "+feature+" where vidid="+str(vidid[0])
        s = self.con.execute(query).fetchone()
		# use pickle to decode NumPy arrays from string
        return pickle.loads(str(s[0]))

 
