def gridChallenge(grid):
    # Write your code here
    sorted_grid=[]
    for i in grid:
        st=''.join(sorted(i))
        sorted_grid.append(st)
    print(sorted_grid)
    for col in zip(*sorted_grid):
        if list(col)!=sorted(col):
            return "NO"
    return "YES"
