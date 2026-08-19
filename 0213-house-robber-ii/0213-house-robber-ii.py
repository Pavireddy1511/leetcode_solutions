class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        memo1=[-1]*n
        memo2=[-1]*n
        rob1=self.recur(n-2,0,nums,memo1)
        rob2=self.recur(n-1,1,nums,memo2)
        return max(rob1,rob2)
    def recur(self,n,st,nums,memo):
        if n==st:
            return nums[st]
        if n==st+1:
            return max(nums[st],nums[st+1])
        if memo[n]!=-1:
            return memo[n]
        memo[n]=max(nums[n]+self.recur(n-2,st,nums,memo),self.recur(n-1,st,nums,memo))
        return memo[n]
