class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res1=0
        res2=0
        for i in range(0,len(nums),1):
            res1=res1^nums[i] & ~res2
            res2=res2^nums[i] & ~res1
        return res1    
            
        
        