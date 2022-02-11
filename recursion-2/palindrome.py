# TRASH

def ph(s,start,end):
    if len(s) == 0:
        return True
    if s[start] == s[end]:
        return True
    else:
        return False
    return ph(s[start:end],start+1,end-1)
def palindrome(s):
    if len(s) == 0 or len(s) ==1:
        return True
    return ph(s,0,len(s)-1)

# CORRECT approach
def pl(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return pl(s,l+1,r-1)

s = input()
l = 0
r = len(s)-1
print(pl(s,l,r))