def marcsCakewalk(calorie):
    # Write your code here
    c=sorted(calorie, reverse=True)
    miles=0
    for i,x in enumerate(c):
        miles+=(2**i)*x
    return miles
