#https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
def removeElement(nums,val):
        count=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
            else:
                continue
        print(count) 
removeElement([3,2,2,3],3)