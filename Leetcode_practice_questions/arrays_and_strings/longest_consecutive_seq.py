#https://leetcode.com/problems/longest-consecutive-sequence/submissions/1956947237/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if not nums:
        return 0;
      nums = set(nums)
      longest = 0
      for x in nums:
         if x - 1 not in nums:
            counter = 1
            while x + counter in nums:
              counter += 1
            longest = max(longest, counter)
      return longest  
