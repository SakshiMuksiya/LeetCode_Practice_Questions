#https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

#Solution
def isSubsequence(s,t) -> bool:
        i,j=0,0
        while i< len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i == len(s)