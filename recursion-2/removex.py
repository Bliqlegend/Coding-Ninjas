def remove(s,x,newS):
    if len(s) == 0:
        return s
    ss = remove(s[1:],x,newS+s)
    if s[0] == x:
        return ''+ss
    else:
        return s[0]+ss

s = "adbef"
x = "f"
newS = remove(s,x,"")
print(newS)