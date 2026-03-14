/**
 * Returns an array where each element is the product of all other elements except itself.
 * @param nums - An array of integers
 * @returns Array with products excluding self
 */
function productExceptSelf_1(nums: number[]): number[] {
    const n = nums.length; 
    const leftProducts = new Array(n).fill(1);
    const rightProducts = new Array(n).fill(1);
    const answer = new Array(n).fill(1); 

    // Calculate prefix products 
    for(let i=1;i<n;i++){
        leftProducts[i] = leftProducts[i-1] * nums[i-1];
    }

    // Calculate suffix products 
    for(let i=n-2;i>=0;i--){
        rightProducts[i] = rightProducts[i+1] * nums[i+1];
    }

    // Put them both together
    for(let i =0;i<n;i++){
        answer[i] = leftProducts[i] * rightProducts[i];
    }

    return answer;

}