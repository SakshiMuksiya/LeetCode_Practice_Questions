#https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150

#solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        index_map={}
        for sc,tc in zip(s,t):
            if sc in index_map:
                if index_map[sc] != tc:
                    return False
            elif tc in index_map.values():
                return False
            index_map[sc]=tc
        return True