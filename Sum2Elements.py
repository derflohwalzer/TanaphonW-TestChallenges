def Sum2Elements(nums, sum):
    length = len(nums)

    # idx1, idx2 = indexes for elements that add up to the sum
    for idx1 in range(length):
        diff = sum - nums[idx1]
        try:
            idx2 = nums.index(diff, idx1 + 1)      #search from index inext  to
            return (idx1,idx2)
        except:
            continue
    
    return None