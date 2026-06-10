class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setn=set(nums)
        return len(setn) < len(nums)
        