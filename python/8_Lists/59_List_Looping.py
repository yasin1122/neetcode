# import used to add type hint for List
from typing import List

def count_x(nums: List[int], x: int) -> int:
    count = 0
    for num in nums:
        if num == x:
            count += 1
    return count

# do not modify below this line
print(count_x([1, 3, 5, 5, 3, 5], 5))