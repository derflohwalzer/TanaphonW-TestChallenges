def ThreeFive():
    
    """ 
    Problem
    Write a function called ThreeFive to print number from 1 to 100 in a new line.
        - if the number is divisible by 3 then print "Three"
        - if the number is divisible by 5 then print "Five"
        - if the number is divisible by both 3 and 5 then print "ThreeFive"
        - Otherwise just print the number
    """
    
    for num in range(100):
        num = num + 1                       # begin at 1, not 0
        if num % 3 == 0 and num % 5 == 0:   # divisible by both 3 and 5
            print("ThreeFive")
        elif num % 3 == 0:                  # divisible by 3
            print("Three")
        elif num % 5 == 0:                  # divisible by 5
            print("Five")
        else:                               # not divisible by 3 or 5
            print(num)
