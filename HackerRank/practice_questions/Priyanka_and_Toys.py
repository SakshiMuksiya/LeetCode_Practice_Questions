#https://www.hackerrank.com/contests/tpinfy007/challenges/priyanka-and-toys

def toys(w):
    # Write your code here
    w=sorted(w)
    container=1
    min_val=w[0]
    for i in range(1,len(w)):
        if w[i]>4+min_val:
            container+=1
            min_val=w[i]
    return container
