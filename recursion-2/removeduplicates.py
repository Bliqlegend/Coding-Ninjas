def removeALLDuplicates(s):
    if len(s) == 0:
        return s
    ss = removeALLDuplicates(s[1:])
    if s[0] in ss:
        return "" + ss
    else:
        return s[0] + ss

def removeCD(s):
    if len(s) == 0:
        return s
    ss = removeCD(s[1:])
    if len(ss) >= 1 and s[0] == ss[0]:
        return "" + ss
    else:
        return s[0] + ss

def TAapproach(s):
    if len(s) == 0:
        return

s = input()
s = removeCD(s)
print(s)