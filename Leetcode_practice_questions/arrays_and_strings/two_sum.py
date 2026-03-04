#https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

#solution
def twoSum(nums, target: int):
        map1={}
        for i,num in enumerate(nums):
            if target-num in map1:
                return[i,map1[target-num]]
            map1[num]=i