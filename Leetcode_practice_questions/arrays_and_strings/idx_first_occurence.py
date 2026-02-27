#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
def strStr(haystack, needle) -> int:
        if len(needle) > len(haystack):
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1