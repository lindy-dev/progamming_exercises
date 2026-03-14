/**
 * Determines if the array contains any duplicate values.
 * @param nums - An array of integers
 * @returns true if any value appears at least twice, false otherwise
 */
function containsDuplicate(nums: number[]): boolean {
    const seen = new Set<number>();

    for (const num of nums) {
        if (seen.has(num)) {
            return true;
        }
        seen.add(num);
    }

    return false;
}