class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        contains = {}
        for num in nums:
            contains[num] = contains.get(num, 0) + 1
            if contains[num] > 1: 
                return True
        
        return False