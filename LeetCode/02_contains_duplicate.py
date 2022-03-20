# Solution for https://leetcode.com/problems/contains-duplicate/
class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        counter = set()

        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True

        return False
