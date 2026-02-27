#https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
def canJump(nums):
        jump=0
        for n in nums:
            if jump<0:
                return False
            elif n>jump:
                jump=n
            jump-=1
        return True