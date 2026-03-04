#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1937921113/?envType=study-plan-v2&envId=top-interview-150

#solution
def twoSum(numbers, target: int) :
       first=0
       last=len(numbers)-1
       while first<last:
        total=numbers[first]+numbers[last]
        if total==target:
            return [first+1,last+1]
        elif total>target:
            last-=1
        else:
            first+=1