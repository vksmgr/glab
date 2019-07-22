'''
this will take care about the file structure for uploading the files and folder to google drive
this module contains the task
    * get the project structure
    * create folder structure to drive
    * create files in the google drive
'''
import collections
import glob

class Files:
    def __init__(self, projRoot):
        '''
        crate the file structure.
        :param projRoot: project root folder path
        '''
        self.projRoot = projRoot
        self.rootFold = projRoot.split('\\')[-1]
        self.files = []
        self.dirs = []

    def getDirs(self):
        '''
        get the directory structure
        it will store the directory in the form of tuple(folderName, parentFolder)
        :return:
        '''
        folders = [f[len(self.projRoot):] for f in glob.glob(self.projRoot + "**/", recursive=True)]
        levDict = collections.defaultdict(set)
        root = self.rootFold
        for fold in folders:
            itme = [fol for fol in fold.split("\\") if len(fol) > 0]
            print(itme)
            for i in range(len(itme)):
                # level_dic[i] = [itme[i]]
                if i == 0:
                    levDict[root].add(itme[i])
                else:
                    levDict[itme[i - 1]].add(itme[i])
        return levDict

    def getFiles(self):
        '''
        this will return the python files with the parent id it also return the defaultdict
        key as the parent name and value as the set.
        :return: tuple.0: contains parent name and files under that folder
                tuple.1: contains name of the file and the path to that file
        '''
        folders = [f[len(self.projRoot):] for f in glob.glob(self.projRoot + "**/*.py", recursive=True)]
        levDict = collections.defaultdict(set)
        fLoc = {}
        for fold in folders:
            try:
                fLoc[fold.split("\\")[-1]] = self.projRoot+fold
            except :
                fLoc[fold.strip("\\")] = self.projRoot+fold
            itme = [fol for fol in fold.split("\\") if len(fol) > 0]
            for i in range(len(itme)):
                if i == 0:
                    if self.chkPy(itme[i]):
                        levDict[self.rootFold].add(itme[i])
                else:
                    if self.chkPy(itme[i]):
                        levDict[itme[i - 1]].add(itme[i])
        print(fLoc)
        print(levDict)
        return levDict, fLoc

    def chkPy(self, filename):
        try:
            ext = filename[-3:]
        except:
            ext = "none"
        if ext == '.py':
            return True
        else:
            return False