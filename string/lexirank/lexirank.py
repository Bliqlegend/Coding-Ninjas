def firstIndex():
    

def permutation():
    n-=1

def lexiRank(s):
    sw = ''.join(sorted(s))
    idx = 1
    mapp = {}
    for i in sw:
        mapp[i] = idx
        idx+=1
    var = 1
    num = 0
    for i in range(len(s)-1,-1,-1):
        num+= mapp[s[i]] * var 
        var*=10
    permutation(num)       
            

s = "cdb"
n = lexiRank(s)
print(n)