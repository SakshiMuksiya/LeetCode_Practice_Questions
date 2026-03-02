#https://leetcode.com/problems/zigzag-conversion/submissions/1935892501/?envType=study-plan-v2&envId=top-interview-150

#solution
def convert(s: str, numRows: int) -> str:
        if s is None and numRows<=0: return ''
        if numRows==1: return s
        result=''
        step=(numRows*2) -2
        for i in range(numRows):
            for j in range(i,len(s),step):
                result+=s[j]
                if i!=0 and i!=numRows-1 and (j+step-2*i)<len(s):
                    result+=s[j+step-2*i]
        return result