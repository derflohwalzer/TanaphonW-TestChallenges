def Sum2Elements(nums: list, sum: int):
    """ 
    Problem
    Given an array of integers nums and an integer sum, 
    return the indexes of 2 elements in the array that add up to the given sum.

    Note
    - There may be duplications in the array
    - The array is not necessarily sorted
    - The may be multiple pairs of elements that add up to the given sum. 
    For simplicity, return only the first pair you can find
    """

    length = len(nums)

    # idx1, idx2 = indexes for elements that add up to the sum
    for idx1 in range(length):
        diff = sum - nums[idx1]
        try:
            idx2 = nums.index(diff, idx1 + 1)       # search from index after idx1, for num[idx2] == diff
            return (idx1,idx2)                      # found matching pair, return output as a tuple
        except:
            continue                                # idx1 cannot match with any number to make sum, go to next idx1
    
    return None                                     # The are no two numbers that add up to sum