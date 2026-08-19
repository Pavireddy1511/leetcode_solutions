class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length=1
        n=len(nums)
        tab=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if(nums[j]<nums[i]):
                    tab[i]=max(tab[i],tab[j]+1)
            length=max(length,tab[i])
        return length      
