class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        memo=[-1]*n
        return self.recur(n-1,nums,memo)
    def recur(self,n,nums,memo):
        if n==0:
            return nums[0]
        if n==1:
            return max(nums[0],nums[1])
        if memo[n]!=-1:
            return memo[n]
        memo[n]=max(nums[n]+self.recur(n-2,nums,memo),self.recur(n-1,nums,memo))
        return memo[n]
           