#https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
def jump(nums) :
    near=far=jumps=0
    while far< len(nums)-1:
        fartest=0
        for i in range (near,far+1):
            fartest=max(fartest,i+nums[i])
        near=far+1
        far=fartest
        jumps+=1
    return jumps