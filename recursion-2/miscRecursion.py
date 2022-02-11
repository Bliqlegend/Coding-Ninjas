def sumdg(n):
    if n == 0:
        return 0
    return int(n%10) + sumdg(n//10)

def zeroesCount(n):
    if n == 0:
        return 0
    if n %10 == 0:
        return 1 + zeroesCount(n//10)
    else:
        return 0 + zeroesCount(n//10)

def stoint(s):
    if len(s) == 1:
        return (ord(s)-48)
    stoint(s[1:])
    return int(s)

def SLOWpairstar(s):
    if len(s) == 1:
        return s
    ss = SLOWpairstar(s[1:])
    if s[0] == s[1]:
        return s[0] + "*"+ ss
    else:
        return s[0] + ss

def FASTpairstar(s):
    if len(s) ==1:
        return s
    if s[0] == s[1]:
        return s[0] + "*" +FASTpairstar(s[1:]) 
    else:
        return s[0] + FASTpairstar(s[1:])
        
# n = int(input())
s = input()
# print(zeroesCount(n))
print(FASTpairstar(s))
