class Solution:
    def climbStairs(self, n: int) -> int:
        tab=[0]*(45)
        tab[0]=1
        tab[1]=2
        tab[2]=3
        for i in range(3,n):
            tab[i]=tab[i-1]+tab[i-2]
        return tab[n-1]    

        