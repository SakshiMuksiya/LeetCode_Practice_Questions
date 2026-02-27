#https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150

#Solution
def productExceptSelf(nums):
        n=len(nums)
        pre_product=1
        post_product=1
        result=[0]*n
        for i in range(n):
            result[i]=pre_product
            pre_product*= nums[i]
        for i in range(n-1,-1,-1):
            result[i]*=post_product
            post_product *=nums[i]
        return result