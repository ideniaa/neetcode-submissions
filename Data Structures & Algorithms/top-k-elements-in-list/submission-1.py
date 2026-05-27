from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []

        # Sort the items by frequency in descending order and take the first k
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            res.append(sorted_items[i][0])

        return list(res)
