class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            x=target-nums[i]
            print(x)
            print(d)
            if x in d:
                return [d.get(x),i]
            else:
                d[nums[i]]=i
        return []
                
