class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = 0
        j = 0
        hashmap = {'T': 0, 'F': 0}
        result = 0

        while j < len(answerKey):
            hashmap[answerKey[j]] += 1
            while min(hashmap['T'], hashmap['F']) > k:
                hashmap[answerKey[i]] -= 1
                i += 1

            result = max(result, j - i + 1)
            j += 1
        return result
