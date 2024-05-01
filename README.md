# Functionality
- function takes two strings word1 and word2 as input and returns a new string by merging the characters of both strings alternately. 

- If one string is longer than the other, the remaining characters from the longer string are appended at the end of the merged string.

```py
    def mergeAlternately(self, word1, word2):
        merged = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        while i < len(word1):
            merged += word1[i]
            i += 1

        while j < len(word2):
            merged += word2[j]
            j += 1

        return merged
```

- If you want to follow any of my challenges made on `Leetcode`, [feel free to follow me](https://leetcode.com/u/castroofelipee/)
