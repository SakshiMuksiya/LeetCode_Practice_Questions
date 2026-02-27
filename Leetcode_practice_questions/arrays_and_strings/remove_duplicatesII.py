#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

#Solution
def removeDuplicates(nums):
        index=1
        occur=1
        for i in range (1,len(nums)):
            if nums[i]==nums[i-1]:
                occur+=1
            else:
                occur=1
            if occur<=2:
                nums[index]=nums[i]
                index+=1
        print (index)
removeDuplicates([1,1,1,2,2,3,3])