class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        result = False
        for i in range(len(nums)):
            if nums[i] in seen:
                result = True
                break
            else:
                seen.append(nums[i])
        
        return result