class Solution:
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


# Test cases
print(Solution().mergeAlternately("abc", "pqr"))
print(Solution().mergeAlternately("ab", "pqrs"))
print(Solution().mergeAlternately("abcd", "pq"))
