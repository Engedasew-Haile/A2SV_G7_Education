"""
Two Sum - O(n) solution using a hash map.

Given an array of integers `nums` and an integer `target`, return indices of the
two numbers such that they add up to `target`.

Assumptions:
- Exactly one solution exists.
- Cannot use the same element twice.

Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return indices of the two numbers such that they add up to target.

    Args:
        nums: list of integers
        target: integer target sum

    Returns:
        A list [i, j] with i != j such that nums[i] + nums[j] == target

    Raises:
        ValueError: if no solution is found (shouldn't happen per problem statement)
    """
    seen = {}  # maps value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    # Example tests from the prompt
    examples = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for nums, target, expected in examples:
        result = two_sum(nums, target)
        print(f"nums={nums}, target={target} -> result={result}, expected={expected}")
        assert set(result) == set(expected), f"Test failed for nums={nums}, target={target}"
    print("All example tests passed.")


    """
Solution.py

Defines class Solution with method twoSum so drivers that call:
    ret = Solution().twoSum(param_1, param_2)
will work.

O(n) time, O(n) space using a dictionary.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers such that they add up to target.

        Args:
            nums: list of integers
            target: integer target sum

        Returns:
            A list [i, j] with i != j such that nums[i] + nums[j] == target
        """
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        # According to the problem there is exactly one solution,
        # but raise an explicit error if none is found.
        raise ValueError("No two sum solution")
        

# Quick self-test when running this file directly.
if __name__ == "__main__":
    examples = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for nums, target, expected in examples:
        result = Solution().twoSum(nums, target)
        print(f"nums={nums}, target={target} -> result={result}, expected={expected}")
        assert set(result) == set(expected)
    print("All example tests passed.")
