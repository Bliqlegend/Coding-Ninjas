def gp(k):
    if k ==0 :
        return 1
    return 1/(2**k) + gp(k-1)

k = int(input())
print(gp(k))
