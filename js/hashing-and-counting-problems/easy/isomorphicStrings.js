/**
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input:
const s = "egg";
const t = "add";

Output: true

Explanation:
The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input:
const s = "f11";
const t = "b23";

Output: false

Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input:
const s = "paper";
const t = "title";

Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
 */

const isIsomorphic = (s, t) => {
  // edge case: if s and t are not the same length return false
  // create 2 maps to store char, index pair of s and t strings
  // iterate of s or t
  // get char of s and t
  // map sChar to tChar in sMap
  // map tChar to sChar in tMap
  // create mapping of sChar -> tChar in sMap and reverse lookup map tMap tChar -> sChar
  // compare if the value in sMap of key sChar is equal to tChar
  // if not return false;
  // default return true;
  if (s.length !== t.length) return false;

  const sMap = new Map();
  const tMap = new Map();

  for (let i = 0; i < s.length; i++) {
    const sChar = s[i];
    const tChar = t[i];
    if (!sMap.has(sChar) && !tMap.has(tChar)) {
      sMap.set(sChar, tChar);
      tMap.set(tChar, sChar);
    }

    if (sMap.get(sChar) !== tChar) return false;
  }

  return true
};

const s = "egg";
const t = "add";

const s2 = "f11";
const t2 = "b23";


const s3 = "badc";
const t3 = "baba";
/**
 * { 'f' => 'b', '1' => '2' }
 * { 'b' => 'f', '2' => '1', '3' => '1' }
 */
// console.log(isIsomorphic(s, t)); // true
// console.log(isIsomorphic(s2, t2)); // false
console.log(isIsomorphic(s3, t3)); // false
