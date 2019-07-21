# import src.main as mn
# mn.entry()

"""
this function will call to the authentication syste
"""
import string
from src.gDrive.gDrive import GDrive

if __name__ == '__main__':
    gd = GDrive()
    drive = gd.authenticate("123")
    # gd.createFile("myupd.txt", "hello nitt", drive)
    data1 = ""
    with open("run.py", 'r') as f:
        data = f.readlines()
        for d in data:
            data1 = data1 + d
        # data = str(data1, 'utf-8')

    # print(data1)
    root = gd.createRootfolder('testProj', drive)
    fid = gd.createFolder("source", root, drive)
    gd.createFileInFolder('main.py', data1, fid, drive)
    print(root)
    print(fid)
    # gd.insert("main.py", data1, drive)



def entry():
    print("This is my work station.")
