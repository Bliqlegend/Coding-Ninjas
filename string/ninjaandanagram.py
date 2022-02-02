from sys import stdin
import sys
sys.setrecursionlimit(10**7)


def OisAnagram(str1, str2) :
    # write your code
    if len(str1) != len(str2):
        return False
    for i in sorted(str1):
        if i not in str2:
            return False
    for i in sorted(str2):
        if i not in str1:
            return False
    
    return True

def SisAnagram(str1,str2):
    count1 = [0 for i in range(26)]
    count2 = [0 for i in range(26)]
    n = len(str1)
    m = len(str2)
    for i in range(n):
        count1[ord(str1[i])-ord('a')]+=1
    for i in range(m):
        count2[ord(str2[i])-ord('a')]+=1
    for i in range(26):
        if count1[i] != count2[i]:
            return False
    return True

# fast input
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    str1 = (n_x[0].strip())
    str2 = (n_x[1].strip())

    return str1, str2

#main

str1, str2 = takeInput()
if (SisAnagram(str1, str2)) :
    print("True")
else :
    print("False")