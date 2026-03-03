#https://leetcode.com/problems/valid-anagram/submissions/1936990888/?envType=study-plan-v2&envId=top-interview-150

#solution
def isAnagram(s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        s_set,t_set=set(s),set(t)
        if len(s_set) != len(t_set): return False
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        return True