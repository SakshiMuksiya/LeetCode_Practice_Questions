def luckBalance(k, contests):
    # Write your code here
    imp,unimp=[],[]
    for l,t in contests:
        if t==0:
            unimp.append(l)
        else:
            imp.append(l)
    luck=sum(unimp)
    imp.sort(reverse=True)
    for i,l in enumerate(imp):
        if i<k:
            luck+=l
        else:
            luck-=l
    return luck
