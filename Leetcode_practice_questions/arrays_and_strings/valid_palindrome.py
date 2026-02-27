#https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

#Solution
def isPalindrome(s):
        string=''.join([i.lower() for i in s if i.isalnum()])
        return string==string[::-1]