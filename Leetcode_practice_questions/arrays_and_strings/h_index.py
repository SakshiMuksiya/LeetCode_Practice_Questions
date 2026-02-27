#https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

#solution
def hIndex(citations) -> int:
        n=len(citations)
        citations.sort()
        for i,v in enumerate(citations):
            if n-i <=v:
                return n-i
        return 0