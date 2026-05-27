class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums_list:
                return [nums_list[res], i]
            else:
                nums_list[nums[i]] = i

        return False
