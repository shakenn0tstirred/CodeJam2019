T = int(input()) # Number of test cases

for i in range(T): # Iterate through each case
    # Initialize/clear lists
    A = []
    B = []
    
    N = input() # Input the total that A and B have to add up to
    
    for j in N:
        if j == "4": # Since the final numbers cannot include the number 4, if a 4 is in the initial number, split it into two 2s
            A.append("2")
            B.append("2")
        else: # If there isn't a 4 in the initial number, keep it as-is in A and maintain B's placement with a 0
            A.append(j)
            B.append("0")
    
    print("Case #" + str(i+1) + ": " + "".join(A) + " " + "".join(B))
