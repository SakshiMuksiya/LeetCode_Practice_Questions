#https://www.hackerrank.com/contests/test-1774426824/challenges/mark-and-toys

def maximumToys(prices, k):
    # Write your code here
    p_s=sorted(prices,reverse=False)
    spent,item_count=0,0
    for i in p_s:
        if i+spent<=k:
            spent+=i
            item_count+=1
        elif i+spent>k:
            pass
    return (item_count)
