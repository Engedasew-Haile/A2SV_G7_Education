from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the number and its index: {number: index}
        num_map = {}
        
        # Iterate over the array with both index and value
        for i, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num
            
            # Check if the complement is already in our dictionary
            if complement in num_map:
                # If found, return the index of the complement and the current index
                return [num_map[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_map[num] = i
            
        return []

# --- Testing the solution with the provided examples ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(f"Example 1: {sol.twoSum([2,7,11,15], 9)}") 
    # Expected: [0, 1]

    # Example 2
    print(f"Example 2: {sol.twoSum([3,2,4], 6)}")     
    # Expected: [1, 2]

    # Example 3
    print(f"Example 3: {sol.twoSum([3,3], 6)}")       
    # Expected: [0, 1]