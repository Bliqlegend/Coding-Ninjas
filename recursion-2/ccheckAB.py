# TRASH AS OF NOW

def checkABHelper(s):
    if len(s) == 1:
        return s
    if s[0] == 'a' and s[1:3]!='a':
        return False 

def checkAB(s):
    if s[0] != 'a':
        return False
    checkABHelper(s)

