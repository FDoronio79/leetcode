/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

Example 1:

Input:
const nums = [1, 2, 3, 1];


Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:

Input:
const nums = [1, 2, 3, 4];


Output: false

Explanation:

All elements are distinct.

Example 3:

Input:
const nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2];


Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
*/

const containsDuplicate = (nums) => {
  const res = {};
  for (const num of nums) {
    if (num in res) {
      return true;
    } else {
      res[num] = 1;
    }
  }
  return false;
};

// Because we are looking for duplicates, we can use Set() which only takes in unique properties
// iterate over the nums array
// check if the set has the number
// if it does then return true
// else add the number to the set
// default return false
const containsDupev2 = (nums) => {
  const tmp = new Set();
  for (const num of nums) {
    if (tmp.has(num)) {
      return true;
    }
    tmp.add(num);
  }
  return false;
};
