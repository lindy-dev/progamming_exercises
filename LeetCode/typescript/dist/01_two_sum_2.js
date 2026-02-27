"use strict";
function twoSum_2(nums, target) {
    // Optimised solution
    // step 1: Create a plain object: Store each number and its index as we iterate through the array
    // step 2: Check Complement: For each number, calculate what value would complete the target (target - current)
    // step 3: Find Match: If complement exists in map, return both indices immediately
    // step 4: Store Current: Add current number to map for future matches
    //Record is a built-in TypeScript utility type that creates an object type where:
    //K = Key type (what the property names are)
    //V = Value type (what the values are)
    const numMap = {};
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (complement in numMap) {
            return [numMap[complement], i];
        }
        numMap[nums[i]] = i;
    }
    throw new Error("No solution found");
}
