class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]

        strs_anagrams = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))

            strs_anagrams[sorted_word].append(word)
        
        return list(strs_anagrams.values())