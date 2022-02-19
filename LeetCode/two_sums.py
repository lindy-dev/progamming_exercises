class Solution:
    def two_sum(self, nums, target):
        complementMap = dict()
        # <7,0> 
        # O(N) 
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            
            if num in complementMap:
                return [complementMap[complement], i]
            else:
                complementMap[complement] = i 

    def bruteforce_two_sum(self, nums, target):
        # Bruteforce solution 
        # O(N^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]