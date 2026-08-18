class Solution:
    def fib(self, n: int) -> int:
        memo=[0]*(30+1)
        if(n==1):
             return 1
        if(n==0):
             return 0
        if(memo[n]!=0):
            return memo[n]
        memo[n]=self.fib(n-1)+self.fib(n-2)
        return memo[n]


        