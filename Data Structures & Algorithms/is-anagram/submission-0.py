class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_anagram = sorted(s)
        t_anagram = sorted(t)

        return s_anagram == t_anagram