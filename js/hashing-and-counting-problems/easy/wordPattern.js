/**
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input:
const pattern = "abba";
const s = "dog cat cat dog";


Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input:
const pattern = "abba";
const s = "dog cat cat fish";


Output: false

Example 3:

Input:
const pattern = "aaaa";
const s = "dog cat cat dog";


Output: false

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
 */
/**
 * @param {string} pattern
 * @param {string} t
 * @return {boolean}
 */
const wordPattern = (pattern, t) => {
    // time comp: O(n) space comp O(n)
    // because t is a phrase, split it into an array to get each individual word property for easier mapping
    // edge case: if pattern length and tArray length are not the same return false
    // create 2 maps 1 for mapping another for reverse look up
    // iterate through pattern and tArray
    // check if current char in pattern is a new key in pattern map and if word is a new key in tMap
    // if it is set key,value pair to respective maps pChar -> word patternMap and word -> pChar in tMap
    // check using pChar to get a value from patternMap and compare if it is not equal to current word
    // default return true
    const tArr = t.split(" ");
    if (pattern.length !== tArr.length) return false;
    
    const patternMap = new Map();
    const tMap = new Map();
    
    for (let i = 0; i < pattern.length; i++) {
        const pChar = pattern[i];
        const word = tArr[i];
        if (!(patternMap.has(pChar)) && !(tMap.has(word))) {
            patternMap.set(pChar, word);
            tMap.set(word, pChar);
        }
        if (patternMap.get(pChar) !== word) return false;
    }
    return true;
}

const p = "abba";
const s = "dog cat cat dog";

const p2 = "abba";
const s2 = "dog cat cat fish";

const p3 = "aaaa";
const s3 = "dog cat cat dog";

console.log(wordPattern(p, s));
console.log(wordPattern(p2, s2));
console.log(wordPattern(p3, s3));