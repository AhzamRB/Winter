def minWindow(log: str, pattern: str) -> str:
    if not log or not pattern:
        return ""

    freq = [0] * 128  #Creates frequency array for ASCII characters so like "A" will be "65" in integer value
    for ch in pattern:
        freq[ord(ch)] += 1 #odr() gets int value of the ASCII char, and this part increments count for each character in pattern

    left = 0 #left pointer for the sliding window, this will shrink when we find req. window 
    needed = len(pattern) #total characters still needed to match
    result = ""

    for right in range(len(log)): #going right first
        if freq[ord(log[right])] > 0: #If char is needed
            needed -= 1
        freq[ord(log[right])] -= 1 #reduce freq for current char

        while needed == 0: #runs after we have valid window
            if not result or (right - left + 1) < len(result): #Checks if the current window is smaller than previous or not
                result = log[left:right+1]

            #Removing left char from window
            freq[ord(log[left])] += 1
            if freq[ord(log[left])] > 0:
                needed += 1
            left += 1

    return result


log = input("Enter log string: ")
pattern = input("Enter pattern string: ")
    
result = minWindow(log, pattern)
print("Smallest substring:", result if result else '""')