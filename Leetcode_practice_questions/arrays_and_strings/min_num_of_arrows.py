#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrows = 1
        end = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > end: 
                arrows += 1  
                end = balloon[1] 
            else:
                end = min(end, balloon[1])
        
        return arrows
