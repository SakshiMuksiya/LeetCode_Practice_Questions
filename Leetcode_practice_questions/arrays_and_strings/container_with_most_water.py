#https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

#solution
def maxArea(height) -> int:
        first,last=0,len(height)-1
        water=0
        while first<last:
            water=max(water, (last-first)*min(height[first],height[last]))
            if height[first]< height[last]:
                first+=1
            else:
                last-=1
        return water