#https://www.hackerrank.com/contests/test-1774426824/challenges/pylons/problem

def pylons(k, arr):
    # Write your code here
    n=len(arr)
    right1=[-1]*n
    last=-1
    for i in range(n):
        if arr[i]==1:
            last=i
        right1[i]=last
    plants=0
    cover=0
    while cover<n:
        hi=min(n-1,cover+k-1)
        best=right1[hi]
        lo=max(0,cover-k+1)
        if best==-1 or best<lo:
            return -1
        plants+=1
        cover=best+k
        
    return plants
