#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

#Solution
def merg(nums1, m ,nums2, n) :
    a,b,idx=m-1,n-1,m+n-1
    while (b>=0 and a>=0):
        if nums1[a]>=nums2[b]:
            nums1[idx]=nums1[a]
            a-=1
        else:
            nums1[idx]=nums2[b]
            b-=1
        idx-=1
    while b>=0:
        nums1[idx]=nums2[b]
        b-=1
        idx-=1
    print(nums1)
merg([1,2,3,0,0,0],3,[2,5,6],3)