#https://leetcode.com/problems/simplify-path/submissions/1965077525/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def simplifyPath(self, path: str) -> str:
        l=[]
        path=path.split('/')
        for i in path:
            if i=='':
                continue
            elif i=="..":
                if l:
                    l.pop()
            elif i==".":
                continue
            else:
                l.append(i)
        return "/"+"/".join(l)
