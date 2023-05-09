
def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lookup = {}
    for idx, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target-num], idx]
        lookup[num] = idx


print(two_sum([11, 23, 9, 15, 17], 24))

"""
PROBLEM :
return the index of number whose sum is equal to target value,
here array is [11, 23, 9, 15, 17] and target value is 24, 
so indices are 2nd and 3rd i.e. return value =[2, 3]
"""