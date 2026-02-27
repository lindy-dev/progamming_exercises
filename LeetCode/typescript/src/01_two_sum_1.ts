function twoSum_1(nums: number[], target: number): number[] {
  // Optimised solution
  // step 1: Create a Map: Store each number and its index as we iterate through the array
  // step 2: Check Complement: For each number, calculate what value would complete the target (target - current)
  // step 3: Find Match: If complement exists in map, return both indices immediately
  // step 4: Store Current: Add current number to map for future matches
  const numMap = new Map<number, number>(); // value -> index

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (numMap.has(complement)) {
      return [numMap.get(complement)!, i];
    }

    numMap.set(nums[i], i);
  }

  // This should never be reached given problem constraints
  throw new Error("No solution found");
}
