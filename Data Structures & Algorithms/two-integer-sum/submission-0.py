from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dictionary to store value:index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:         # Check if the needed pair is already stored
                return [seen[diff], i]  # Return indices in correct order
            seen[num] = i           # Store current number's index
        return []  # This line is just a fallback (problem guarantees a solution)
