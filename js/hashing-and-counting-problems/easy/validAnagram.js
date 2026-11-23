/**
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input:
const s = "anagram";
const t = "nagaram";


Output: true

Example 2:

Input:
const s = "rat";
const t = "car";


Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 */

const validAnagram = (s, t) => {
  if (s.length !== t.length) return false;

  const count = {};
  for (const char of s) count[ch] = (count[ch] || 0) +1;

  for (const char of t) {
      if (!count[char]) return false;
      count[char]--;  
  }
  return true
};

const s = "aaaabbbbeeeccooosdddd";
const t = "abb";

console.log(validAnagram(s, t));
