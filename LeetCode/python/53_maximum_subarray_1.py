from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)
            
            # Max crossing sum
            cross_left = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                cross_left = max(cross_left, current_sum)
            
            cross_right = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                cross_right = max(cross_right, current_sum)
            
            return max(left_max, right_max, cross_left + cross_right)
        
        return helper(0, len(nums) - 1)
