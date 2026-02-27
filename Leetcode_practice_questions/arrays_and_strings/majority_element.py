#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

#Solution
def majorityElement(nums):
        n=(len(nums)//2)+1
        lst={}
        for i in nums:
            if i in lst:
                lst[i]+=1
            else:
                lst[i]=1
        for k,v in lst.items():
            if v>=n:
                return k