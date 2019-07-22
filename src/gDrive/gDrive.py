'''
This module is used for the google drive attachement it will upload the files to google drive if
there is any change in the file. if there are no changes in the file it will not upload that file.

mainly this module has divided into three parts

        * Getting drive authentication (if possible Only once and Automatic)
        * check whether files are modified or not
        * Upload only those files which are modified.
'''

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json

import logging

logging.basicConfig(filename='gdrive.log', level=logging.DEBUG)


class GDrive:
    def __init__(self):
        logging.info("Starting Gdrive...")
        '''
        initialize the constructor
        '''
        self.db = LocalDB()

    def authenticate(self, key):
        '''
        this method will authenticate to the google server by taking the key
        :param key:
        :return: it will return the object of drive.
        '''
        try:
            gauth = GoogleAuth()
            gauth.LocalWebserverAuth()
            return GoogleDrive(auth=gauth)
        except:
            logging.error("Error while authentication")
            print("Error While Authentication.")
            return None

    def insert(self, fname, data, drive):
        """
        this function will insert data to google drive in both cases if the file is present in the drive it will
        update that file. if file not present in the drive then it will create the file and then insert data
        :param fname: name of the file
        :param data: string which going to be saved on google drive
        :param drive: it's drive object
        :return: none
        """
        try:
            fId = self.db.getValue(fname)
            gfile = drive.CreateFile({'id': fId})
            if fId is None: 1/0
            self.updateFile(gfile, data)
        except:
            self.createFile(fname, data, drive)

    def createFile(self, fileName, data, drive):
        file = drive.CreateFile({'title': fileName})
        file.SetContentString(str(data))
        file.Upload()
        self.db.update(fileName, file['id'])

    def updateFile(self, gfile, data):
        '''
        it will update the existing file content in the google drive
        :param id: google drive file id
        :param data: data which need to be updated
        :return: none
        '''
        # first create file instance using file id
        try:
            gfile.SetContentString(str(data))
            gfile.Upload()
        except:
            logging.error("Error while updating file ")

    def createFolder(self, folderName, parentId, drive):
        '''
        this function will create folder inside the google dive in parent folder id
        :param folderName:
        :param parentId:
        :param drive:
        :return:
        '''
        fid = self.db.getValue(folderName)
        if fid:
            return fid
        else:
            folder = drive.CreateFile({
                'title': folderName,
                'parents': [{'id': parentId}],
                'mimeType': 'application/vnd.google-apps.folder'
            })
            folder.Upload()
            self.db.update(folderName, folder['id'])
            return folder['id']

    def createRootfolder(self, folderName, drive):
        '''
        this will create the root folder inside the google drive
        :param folderName: root folder name
        :param drive: google drive object
        :return: root folder id
        '''
        fid = self.db.getValue(folderName)
        if fid:
            return fid
        else:
            root = drive.CreateFile({
                'title': folderName,
                'mimeType': 'application/vnd.google-apps.folder'
            })
            root.Upload()
            self.db.update(folderName, root['id'])
            return root['id']

    def createFileInFolder(self, fileName, data, parentFolderID, drive):
        '''
        this will create file in the specific folder in google drive.
        :param fileName: name of the file
        :param data: which need to be written inside file
        :param parentFolderID: parent folder in which we need to write the file
        :param drive: Google Drive object
        :return: None
        '''
        file = drive.CreateFile({
            'title': fileName,
            'parents': [{'kind': 'drive#fileLink', 'id': parentFolderID}]
        })
        file.SetContentString(str(data))
        file.Upload()
        self.db.update(fileName, file['id'])
    def getId(self, key):
        '''
        this function will return the id of the associated key
        :param key: it is the name of the file
        :return: this will return associate google drive file id
        '''
        return self.db.getValue(key)

class LocalDB:
    '''
    this is the file name and there id local database to work with the google
    Drive
    '''

    def __init__(self):
        self.dbName = "meta.json"
        self.dbData = {}
        self.loadData()

    def loadData(self):
        '''
        this will initially load the data to the dict
        :return:
        '''
        try:
            with open('meta.json', 'r') as f:
                self.dbData = json.load(f)
        except:
            logging.warning("Metadata File is Empty")

    def createDb(self):
        '''
        this function will crete the json file database if not exist and return the dict
        :return:
        '''
        with open('meta.json', 'w') as f:
            json.dump({"ver": 0.1}, f)

    def update(self, id, value):
        '''
        this will insert the deta and update if does not exist in the file
        :param id: Key
        :param value: value
        :return: none
        '''
        with open('meta.json', 'w+') as f:
            try:
                self.dbData[str(id)] = value
            except:
                print("error while inserting the key value")
                logging.error("Error while inserting key value")
            json.dump(self.dbData, f)

    def getValue(self, id):
        '''
        this function will return value by taking the id
        :param id: key
        :return: value
        '''
        return self.dbData.get(id)
