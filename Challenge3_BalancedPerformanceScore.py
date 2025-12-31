def median_merge(scoresA, scoresB):
    scores = sorted(scoresA + scoresB)
    n = len(scores)
    if n % 2 == 1:
        return scores[n//2]
    else:
        return (scores[n//2 - 1] + scores[n//2]) / 2


print(median_merge([1,3], [2]))
print(median_merge([1,2], [3,4]))