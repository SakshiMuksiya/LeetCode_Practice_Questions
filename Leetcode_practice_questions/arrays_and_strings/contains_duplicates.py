#https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150

#solution
def containsNearbyDuplicate(self, nums, k: int) -> bool:
        win=set()
        for i in range(len(nums)):
            if nums[i] in win:
                return True
            win.add(nums[i])
            if len(win)>k:
                win.remove(nums[i-k])
        return False