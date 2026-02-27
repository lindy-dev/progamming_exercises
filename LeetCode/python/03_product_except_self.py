# Solution for https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def product_except_self(self, nums):
        before = [1] * len(nums)
        after = [1] * len(nums)
        product = [0] * len(nums)

        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            after[i] = after[i+1] * nums[i+1]

        for i in range(0, len(nums)):
            product[i] = before[i] * after[i]

        return product

    def memory_optimised_product_except_self(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= num[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= num[i]

        return res
