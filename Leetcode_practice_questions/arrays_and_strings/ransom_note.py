#https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

#solution
def canConstruct(ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine=magazine.replace(c,'',1)
        return True