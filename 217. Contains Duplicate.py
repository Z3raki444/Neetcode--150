class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)

        n_modified = len(set(nums))
        
        if n == n_modified:
            return False
        else:
            return True

