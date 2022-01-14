# memoization
def lcs(str1,str2,i,j,dp):
    if i==len(str1) and j==len(str2):
        return 0
    if str1[i] == str2[j]:
        if dp[i+1][j+1] == -1:
            smallans = lcs(str1,str2,i+1,j+1,dp)
            dp[i+1][j+1] = smallans
            ans =  1 + smallans
        else:
            ans = 1 + dp[i+1][j+1]
    else:
        if dp[i][j+1] == -1:
            ans1 = lcs(str1,str2,i,j+1,dp)
            dp[i][j+1] = ans1
        else:
            ans1 = dp[i][j+1]
        if dp[i+1][j] == -1:
            ans2 = lcs(str1,str2,i+1,j,dp)
            dp[i+1][j] = ans2
        else:
            ans2 = dp[i+1][j] 
        ans = max(ans1,ans2)
    return ans


mRows = len(str1)
nCols = len(str2)
dp =[[-1 for j in range(mRows+1)] for i in range(nCols+1)]
