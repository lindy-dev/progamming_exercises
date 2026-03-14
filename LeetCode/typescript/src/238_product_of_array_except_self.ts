/**
 * Returns an array where each element is the product of all other elements except itself.
 * @param nums - An array of integers
 * @returns Array with products excluding self
 */
function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const answer:number[] = new Array(n).fill(1);

    // First pass: Calculate the prefix products 
    let leftProduct = 1; 
    for(let i=0;i<n;i++){
        answer[i] = leftProduct;
        leftProduct = leftProduct * nums[i];
    }

    // Second pass: Calculate the suffix products
    let rightProduct = 1; 
    for(let i=n-1;i>-1;i--){
        answer[i] = answer[i] * rightProduct;
        rightProduct = rightProduct * nums[i];
    }
    return answer;
}