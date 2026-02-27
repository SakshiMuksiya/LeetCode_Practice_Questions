#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

#Solution
def rotate(nums, k):
        n=len(nums)
        if n==0:
            pass
        else:
            k=k%n
            nums[:n-k]=reversed(nums[:n-k])
            nums[n-k:]=reversed(nums[n-k:])
            nums[:]=reversed(nums)
        