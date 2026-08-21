class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for _ in range(n)]
        rb=0
        cb=0
        re = n-1
        ce = n - 1
        num=1
        while rb<=re and cb<=ce:
            #right
            for i in range(cb,ce+1):
                res[rb][i]=num
                num+=1
            rb+=1
            #down
            for j in range(rb,re+1):
                res[j][ce]=num
                num+=1
            ce-=1
            #left
            if rb<=re:
                for k in range(ce,cb-1,-1):
                    res[re][k]=num
                    num+=1
                re-=1
            #up
            if cb<=ce:
                for l in range(re,rb-1,-1):
                    res[l][cb]=num
                    num+=1
                cb+=1
        return res 
        