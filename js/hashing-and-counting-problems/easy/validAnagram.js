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
  for (const char of s) count[ch] = (count[ch] || 0) + 1;

  for (const char of t) {
    if (!count[char]) return false;
    count[char]--;
  }
  return true;
};

const isAnagram = (s, t) => {
  // check if both strings are the same length, if not return flase;
  // get a count of each letter in string s in a Map
  // iterate through string t
  // if letter is in the s Map decrement the letter's value
  // check if there are any non 0 values left
  if (s.length !== t.length) return false;
  const sCount = new Map();
  for (const char of s) {
    sCount.set(char, (sCount.get(char) ?? 0) + 1);
  }
  for (const char of t) {
    if (!sCount.get(char)) {
      return false;
    }

    sCount.set(char, sCount.get(char) - 1);
  }

  return true;
};

const s = "aaaabbbbeeeccooosdddd";
const t = "abb";

console.log(validAnagram(s, t));
