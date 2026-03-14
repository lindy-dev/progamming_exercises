def maxProduct(nums: list[int]) -> int:
    """
    Find the maximum product subarray using dynamic programming.
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only tracking two variables
    """
    if not nums:
        return 0
    
    # Initialize with first element
    max_ending_here = nums[0]
    min_ending_here = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        
        # If current number is negative, swap max and min
        # (negative × negative = positive, so min becomes max candidate)
        if num < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here
        
        # Update max and min ending at current position
        # Either start fresh from current number or extend previous subarray
        max_ending_here = max(num, max_ending_here * num)
        min_ending_here = min(num, min_ending_here * num)
        
        # Update global result
        result = max(result, max_ending_here)
    
    return result
