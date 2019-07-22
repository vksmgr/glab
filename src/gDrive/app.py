import logging

from gDrive.gDrive import GDrive
from gDrive.files import Files


class App():
    '''
    this application start
    '''

    def __init__(self, projPath):
        '''
        constructor
        '''
        self.projPath = projPath
        self.gd = GDrive()
        self.drive = self.gd.authenticate('key')
        self.fls = Files(projPath)
        pass

    def run(self):
        '''
        this method will loop the application and it's the starting point of the application
        :return:
        '''
        self.start()
        # while True:
        #     self.start()

    def start(self):
        '''
        this methd will be called to create the file folder in the drive at start.
        this method will create project from scrach in the google drive.
        :return: none
        '''

        ## first create all directories
        dirs = self.fls.getDirs()
        rootFoldId = self.gd.createRootfolder(self.projPath.split('\\')[-1], self.drive)
        for dir, values in dirs.items():
            fId = self.gd.getId(dir)
            for fol in values:
                self.gd.createFolder(fol, fId, self.drive)

        ## now create the files in the that specific directoriess
        print("you enterd here ::::: ")
        files, fpaths = self.fls.getFiles()
        # print("Debug1: ", files)
        # print("Debug2: ", fpaths)
        for parent, childs in files.items():
            if parent == "" or parent is None :
                parentId = rootFoldId
            else:
                parentId = self.gd.getId(parent)
            # print("Parent {} => parent Id : {}".format( parent, parentId))
            for file in childs:
                self.gd.createFileInFolder(file, self.getData(fpaths.get(file)), parentId, self.drive)

    def getData(self, filePath):
        '''
        open the file and get the data inside it
        handle the exception
        :param filePath: path to the specific file
        :return: return the data in the text format
        '''
        # print("Debug : ", filePath)
        try:
            temp = ""
            with open(str(filePath), 'r') as f:
                data = f.readlines()
                for line in data:
                    temp = temp + line
            return temp
        except:
            logging.error("error occured while opening the file")
            print('error while opening the files')
            return None

    def update(self):
        '''
        this method will update the changes in google drive.
        update the files in google drive.
        update only those files which are modified
        :return: none
        '''
        pass
