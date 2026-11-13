class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        result = False
        for i in range(len(nums)):
            if nums[i] in seen:
                result = True
                break
            else:
                seen.add(nums[i])
        
        return result