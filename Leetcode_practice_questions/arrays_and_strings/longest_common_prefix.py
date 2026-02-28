#https://leetcode.com/problems/longest-common-prefix/submissions/1933284723/?envType=study-plan-v2&envId=top-interview-150

#Solution
def longestCommonPrefix(strs) -> str:
    ans=''
    v=sorted(strs)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return ans
        ans+=first[i]
    return ans