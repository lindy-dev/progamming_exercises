from typing import List
class Solution:
    

    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Step 0 loop through entire
        # Step 1 Identify duplicates
        # Step 2 If duplicate, shift elements to left, replace with dummy 
        # Step 3 else do nothing
        # Step 4 count unique
        if not nums:
            return 0

        k = 1  # The first element is always unique by default
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k