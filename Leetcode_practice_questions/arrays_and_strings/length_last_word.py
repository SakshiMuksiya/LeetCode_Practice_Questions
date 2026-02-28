#https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

#Solution
def lengthOfLastWord(s: str) -> int:
    words=s.strip().split()
    if not words:
        return 0
    return(len(words[-1]))