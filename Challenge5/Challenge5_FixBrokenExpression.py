def removeInvalidParentheses(expr):

    #Checks for validity of ()
    def isValid(string):
        count = 0
        for character in string:
            if character == '(':
                count += 1
            elif character == ')':
                count -= 1
                if count < 0: 
                    return False
        return count == 0

    #BFS
    queue = {expr}  #Using set as a queue, handles duplicates at same level
    visited = {expr} #To track visited strings
    found = False
    result = []

    while queue:
        #Check first level
        for string in queue:
            if isValid(string):
                result.append(string)
                found = True
        
        #If valid strings are found, result is returned
        if found:
            return result
        
        #Generates next level if no valid strings are found
        next_level = set()
        for string in queue:
            for i in range(len(string)):
                #Only remove parentheses, not letters
                if string[i] not in "()":
                    continue
                
                #Creates a new string without the character at index i
                next_string = string[:i] + string[i+1:]
                
                if next_string not in visited:
                    next_level.add(next_string)
                    visited.add(next_string)
        
        queue = next_level

    return result


test_cases = [
    "()())()",
    "(a)())()",
    ")(",
    "()",
    "abc",
    "((("
]

for expr in test_cases:
    print(f"Input:  {expr}")
    print(f"Output: {removeInvalidParentheses(expr)}\n")