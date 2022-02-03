def permutation(s,on,output):
    if len(s) == 0:
        output.append(on)
        return 

    for i in range(len(s)):
        ch = s[i]
        left = s[0:i]
        right = s[i+1:]
        rest = left + right
        permutation(rest,on + ch,output)
    return output


def lexiRank(s):
    sw = ''.join(sorted(s))
    output = permutation(sw,"",[])
    n = output.index(s)+1
    return n