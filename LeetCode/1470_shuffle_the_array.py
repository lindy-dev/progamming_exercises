def rearrange_array(nums):
    n = len(nums) // 2
    x_elements = nums[:n]
    y_elements = nums[n:]
    
    result = []
    for i in range(n):
        result.append(x_elements[i])
        result.append(y_elements[i])
    
    return result

# Example usage:
nums = [2, 5, 1, 3, 4, 7]
result = rearrange_array(nums)
print(result)  # Output: [2, 3, 5, 4, 1, 7]