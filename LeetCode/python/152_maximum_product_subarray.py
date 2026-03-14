def maxProductTwoPass(nums: list[int]) -> int:
    """
    Alternative: Track products from left-to-right and right-to-left.
    Handles cases where subarray starts from middle.
    """
    n = len(nums)
    result = float('-inf')
    
    # Left to right pass
    product = 1
    for num in nums:
        product *= num
        result = max(result, product)
        if product == 0:
            product = 1  # Reset after zero
    
    # Right to left pass (catches cases like [-2, 0, -1] where max is 0)
    product = 1
    for num in reversed(nums):
        product *= num
        result = max(result, product)
        if product == 0:
            product = 1
    
    return result