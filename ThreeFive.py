def ThreeFive():
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
