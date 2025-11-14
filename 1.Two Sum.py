class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        resulthash = {}   

        for i, num in enumerate(nums):
            difference = target - num

            if difference in resulthash:
                return [resulthash[difference], i]

            resulthash[num] = i