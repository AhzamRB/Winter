def median_merge(scoresA, scoresB):

    n, m = len(scoresA), len(scoresB)
    total_length = n + m #Only combined length this time
    a = b = 0 #Random pointers for both scores
    previous = current = 0 #Current contains the current value, previous contains the value before it

    for _ in range((total_length // 2) + 1): #Cause we can stop in the middle instead of going all the way

        previous = current #Cause we need the previous value for even length arrays

        #This part selects the smaller value from both and increments the pointer for the one it selected
        # b>=m is for when scoresB runs out of scores
        # scoresA[a] <= scoresB[b], pick from A if A[a] is smaller or equal
        if a < n and (b >= m or scoresA[a] <= scoresB[b]):
            current = scoresA[a]
            a += 1
        else:
            current = scoresB[b]
            b += 1

    if total_length % 2 == 0:
        return (previous + current) / 2
    return current


print(median_merge([1,3], [2]))
print(median_merge([1,2], [3,4]))