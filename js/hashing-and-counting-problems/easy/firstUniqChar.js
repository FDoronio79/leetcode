/**
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input:
const s = "leetcode";


Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input:
const s = "loveleetcode";


Output: 2

Example 3:

Input:
const s = "aabb";


Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
 */

const firstUniqChar = (s) => {
    // solution O(n) =
    // edge case: return 0 if length of string is 1 don't need to write because it's handle in the loop
    // create a Map to keep track of chars and their count
    // iterate over s to count each char
    // iterate over char s again
    // check which char has the first count of 1 and return the index
    // default: return -1 if no unique chars

    const charsMap = new Map();

    for (let i = 0; i < s.length; i++) {
        const currChar = s[i];
        charsMap.set(currChar, (charsMap.get(currChar) ?? 0) + 1);
    }

    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (charsMap.get(char) === 1) return i;
    }

    return -1;
}

const s = "leetcode";
const s2 = "loveleetcode";
const s3 = "aabb";

console.log(firstUniqChar(s))
console.log(firstUniqChar(s2))
console.log(firstUniqChar(s3))

