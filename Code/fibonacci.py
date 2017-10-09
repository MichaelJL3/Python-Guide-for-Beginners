"""Fibonacci in python with lookup table"""

def fib(x, fibLookup={0:0, 1:1}):
    """Looks up the nth fibonnaci number
        uses an enclosed lookuptable to remember
        values while used and not having global exposure
        the lookup table can be overwritten if one is provided
    """

    if x <= 0:
        return 0
    elif x == 1:
        return 1

    try:
        return fibLookup[x]
    except:
        answer = fib(x - 1, fibLookup) + fib(x - 2, fibLookup)
        fibLookup[x] = answer
        return answer

if __name__ == "__main__":
    #enter in value
    try:
        x = int(input("Enter terms to display: "))
    except:
        print("Must enter in a valid integer")
        exit(1)

    #create lookup table for displaying all terms rather than one
    lookup = {0:0,1:1}

    #fibonnaci(x)
    ans = fib(x, lookup)
    
    #display sequence
    for i in range(x):
        print(lookup[i])
