#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
def removeDuplicates(nums):
    nums[:]=sorted(set(nums))
    print( len(nums))
removeDuplicates([1,1,2])