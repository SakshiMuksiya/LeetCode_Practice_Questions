#https://www.hackerrank.com/contests/test-1774426824/challenges/largest-permutation

def largestPermutation(k, arr):
    # Write your code here
    n=len(arr)
    pos={v:i for i,v in enumerate(arr)}
    for i in range(n):
        if k==0:
            break
        if arr[i]==n-i:
            continue
        target=n-i
        j=pos[target]
        pos[arr[i]]=j
        pos[target]=i
        arr[i],arr[j]=arr[j],arr[i]
        k-=1
    return arr
