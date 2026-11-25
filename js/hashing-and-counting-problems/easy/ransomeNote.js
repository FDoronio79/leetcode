/**
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input:
const ransomNote = "a";
const magazine = "b";

Output: false
Example 2:

Input:
const ransomNote = "aa";
const magazine = "ab";

Output: false
Example 3:

Input:
const ransomNote = "aa";
const magazine = "aab";

Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
 */

const canConstruct = (ransomNote, magazine) => {
  if (magazine.length < ransomNote) return false;

  const magCount = new Map();
  for (const char of magazine) {
    magCount.set(char, (magCount.get(char) ?? 0) + 1);
  }

  for (const char of ransomNote) {
    if (!magCount.get(char)) {
      return false;
    }
    magCount.set(char, magCount.get(char) - 1);
  }
  return true;
};
