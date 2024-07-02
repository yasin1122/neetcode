from typing import List

def get_sum(nums: List[int]) -> int:
    # return sum(nums)
    total = 0
    for num in nums:
        total += num
    return total

def get_min(nums: List[int]) -> int:
    # return min(nums)
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

get_max = lambda nums: max(nums)

# do not modify below this line
print(get_sum([1, 3, 5, 2]))
print(get_min([1, 3, 5, 2, -5]))