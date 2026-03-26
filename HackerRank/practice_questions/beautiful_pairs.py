#https://www.hackerrank.com/contests/tpinfy007/challenges/beautiful-pairs/problem
from collections import Counter
def beautifulPairs(A, B):
    # Write your code here
    freq=Counter(B)
    matches=0
    for i in A:
        if freq[i]>0:
            matches+=1
            freq[i]-=1
    if matches<len(A):
        return matches+1
    else:
        return matches-1
