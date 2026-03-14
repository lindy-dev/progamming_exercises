from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set and store each value
        # Loop through the list 
        # Check if there is a duplicate in the set 
        # If there is a duplicate, then break out of the loop and return true
        # Else return false 
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False