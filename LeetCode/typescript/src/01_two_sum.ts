function twoSum(nums: number[], target: number): number[] {
  // Brute force solution
  // step 1 loop through all the num in nums
  // step 2 nested loop through remaining num in nums
  // step 3 add both the nums from loop 1 and loop 2
  // step 4 see if they add up to target
  // step 5 if they add up to target then break the loop
  // step 6 if they don't then continue the loop

  let solutionIndices: number[] = [];
  for (let i: number = 0; i < nums.length; i++) {
    for (let j: number = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        solutionIndices.push(i);
        solutionIndices.push(j);
        break;
      }
    }
  }
  return solutionIndices;
}
