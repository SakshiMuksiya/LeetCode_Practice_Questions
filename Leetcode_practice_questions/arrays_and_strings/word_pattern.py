#https://leetcode.com/problems/word-pattern/submissions/1936973179/?envType=study-plan-v2&envId=top-interview-150

#solution
def wordPattern(pattern: str, s: str) -> bool:
        words=s.split(' ')
        if len(words)!=len(pattern): return False 
        return len(set(pattern)) == len(set(words))==len(set(zip(pattern,words)))