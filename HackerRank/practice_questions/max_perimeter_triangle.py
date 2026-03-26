#https://www.hackerrank.com/contests/tpinfy007/challenges/maximum-perimeter-triangle/problem

def maximumPerimeterTriangle(sticks):
    # Write your code here
    s=sorted(sticks)
    for i in range(len(s)-1,1,-1):
        a,b,c=s[i],s[i-1],s[i-2]
        if c+b>a:
            return c,b,a
    return [-1]
