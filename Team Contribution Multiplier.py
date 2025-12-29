#Task 1

def TeamContribution(contributions):
    length = len(contributions)
    prefix = 1 #To calculate stuff to the left of current index
    suffix = 1 #To calculate stuff to the right of current index

    result = [1]*length #Result vector, currently all 1s, will be updated in loops

    #Calculating prefix part
    for i in range(length): 
        result[i] = result[i] * prefix # [[1*1], [1*1], [1*2], [1*6]]
        prefix = prefix * contributions[i] #Prefix will update like: intial(1) > 1 > 2 > 6 > 24 (for 4 iterations)
    
    print(f"Result after prefix part: {result}")
    print(f"Prefix: {prefix}")

    #Calculating suffix part
    for i in range(length-1, -1, -1): #Now start backwards so [6, 2, 1, 1] will be multiplied by suffix values
        result[i] = result[i] * suffix  # [1, 1, 2, 6] * [24, 12, 4, 1]
#                                                   ^                ^
        suffix = suffix * contributions[i]

    print(f"Suffix: {suffix}")

    return result

#O(n) complexity for time

contributions = []
n = int(input("Enter the number of team members: "))
for x in range(n):
    contribution = int(input(f"Enter the contribution of team member {x+1}: "))
    contributions.append(contribution)

print(TeamContribution(contributions))