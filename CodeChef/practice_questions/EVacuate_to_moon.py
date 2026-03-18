#https://www.codechef.com/practice/course/greedy-algorithms/INTGRA01/problems/MOONSOON

# cook your dish here
def total_energy(energy_cars, power_outlets, num_hrs):
    e=sorted(energy_cars,reverse=True)
    p=sorted(power_outlets, reverse=True)
    loop=min(len(e),len(p))
    watt=0
    for i in range(loop):
        w=p[i]*num_hrs
        if w>e[i]:
            watt+=e[i]
        else:
            watt+=w
    print(watt)
    
cases=int(input())
for _ in range(cases):
    num_cars, num_outlets, num_hrs=input().split()
    energy_cars=list(map(int, input().split()))
    power_outlets=list(map(int, input().split()))
    total_energy(energy_cars, power_outlets, int(num_hrs))
