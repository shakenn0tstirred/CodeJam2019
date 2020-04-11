T = int(input()) # Number of cases

for i in range(T):
    N = int(input()) # Maze dimensions
    P = input() # Lydia's valid maze path
    y = [] # This will be the program's valid path
    
    for j in P: # The program will "mirror" Lydia's path
        if j == 'E':
            y.append('S')
        else:
            y.append('E')
    
    print("Case #" + str(i+1) + ": " + "".join(y))
