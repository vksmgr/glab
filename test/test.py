import glob
import collections
from src.gDrive.files import Files

# path = "G:\PycharmWorkspace\odrive\Google Drive\glab\\"
# folders  = [ f[len(path): ] for f in glob.glob(path + "**/*.py", recursive=True)]
#
# for fold in folders:
#     print(fold)

#
# def chkPy(filename):
#     try:
#         ext = filename[-3:]
#     except:
#         ext = "none"
#     if ext == '.py':
#         return True
#     else:
#         return False
#     # if
#
#
# import re
#
# path = "G:\PycharmWorkspace\odrive\Google Drive\glab\\"
# folders = [f[len(path):] for f in glob.glob(path + "**/", recursive=True)]
# tmp = []
# levDict = collections.defaultdict(set)
# level_dic = {}
# root = 'glab'
# patt = r'*.py'
#
# for fold in folders:
#     itme = [fol for fol in fold.split("\\") if len(fol) > 0]
#     # print(itme)
#     for i in range(len(itme)):
#         # level_dic[i] = [itme[i]]
#         if i == 0:
#             # if chkPy(itme[i]):
#             levDict[root].add(itme[i])
#         else:
#             # if chkPy(itme[i]):
#             levDict[itme[i - 1]].add(itme[i])
#
# for key, values in levDict.items():
#     print(key)
#     print(values)
#
# #     print(fold.split('\\'))
# # print( tmp)
# # chkPy("main.py")
# fl = Files("G:\PycharmWorkspace\odrive\Google Drive\glab")
# files, filePaths = fl.getFiles()
# print(files)
# for parent, childs in files.items():
#     print(parent)
#     for file in childs:
#         print(filePaths.get(file))
#     print(childs)
# print(filePaths)

## testing
temp = " "
with open(str('G:\PycharmWorkspace\odrive\Google Drive\glab\src\main.py'), 'r') as f:
    data = f.readlines()
    for line in data:
        temp = temp + line

print(temp)
