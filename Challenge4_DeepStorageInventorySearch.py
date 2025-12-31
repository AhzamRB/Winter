import heapq

def kthSmallest(matrix, k):

    rows = len(matrix)
    cols = len(matrix[0])
    
    #Heap's gonna store tuples(value, row_index, col_index)
    min_heap = []

    for r in range(min(rows, k)): #min(rows, k) cause the required value will be in a row index less than or equal to k.
        value = matrix[r][0] #First element of each row 
        heapq.heappush(min_heap, (value, r, 0))

    #Count for the number of elements popped from the heap
    n = 0
    while min_heap:
        value, r, c = heapq.heappop(min_heap)
        n += 1
        
        if n == k:
            return value
        
        #this part pushes the next element of the same row into the heap
        next_col = c + 1
        if next_col < cols:
            next_val = matrix[r][next_col]
            heapq.heappush(min_heap, (next_val, r, next_col))

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]

k = int(input("Enter the value of k: "))
print(kthSmallest(matrix, k))
