class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashResult = {} 
        for num in nums: 
            if num not in HashResult: 
                HashResult[num] = nums.count(num)
            
        sorted_hash = sorted(HashResult.items(), key=lambda x: x[1], reverse=True) 
            
        result = [num for num, freq in sorted_hash[:k]]

        return result