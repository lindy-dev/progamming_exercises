def removeElement(nums, val):
    k = 0  # Initialize a pointer for the next position of non-val elements

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k

# Example usage:
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print("Number of elements not equal to val:", k)  # Output: 2
print("Array with non-val elements at the beginning:", nums[:k])  # Output: [2, 2]