import glob
import collections

# path = "G:\PycharmWorkspace\odrive\Google Drive\glab\\"
# folders  = [ f[len(path): ] for f in glob.glob(path + "**/*.py", recursive=True)]
#
# for fold in folders:
#     print(fold)


def chkPy(filename):
    try:
        ext = filename[-3:]
    except :
        ext = "none"
    if ext =='.py':
        return True
    else:
        return False
    # if

import re
path = "G:\PycharmWorkspace\odrive\Google Drive\glab\\"
folders  = [ f[len(path): ] for f in glob.glob(path + "**/*.py", recursive=True)]
tmp = []
levDict = collections.defaultdict(set)
level_dic= {}
root = 'myProj'
patt = r'*.py'

for fold in folders:
    itme = [fol for fol in fold.split("\\") if len(fol) > 0]
    # print(itme)
    for i in range(len(itme)):
        # level_dic[i] = [itme[i]]
        if i == 0:
            if chkPy(itme[i]):
                levDict[root].add(itme[i])
        else:
            if chkPy(itme[i]):
                levDict[itme[i-1]].add(itme[i])

print(levDict.items())

#     print(fold.split('\\'))
# print( tmp)
chkPy("main.py")
