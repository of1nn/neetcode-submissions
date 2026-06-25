class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        decrease_dict = {}
        for ind, num in enumerate(nums):
            if target - num in decrease_dict:
                return [decrease_dict[target - num], ind]
            decrease_dict[num]=ind