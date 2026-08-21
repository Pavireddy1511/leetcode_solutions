class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        rb=0
        cb=0
        re = len(matrix)-1
        ce = len(matrix[0]) - 1
        while rb<=re and cb<=ce:
            #right
            for i in range(cb,ce+1):
                res.append(matrix[rb][i])
            rb+=1
            #down
            for j in range(rb,re+1):
                res.append(matrix[j][ce])
            ce-=1
            #left
            if rb<=re:
                for k in range(ce,cb-1,-1):
                    res.append(matrix[re][k])
                re-=1
            #up
            if cb<=ce:
                for l in range(re,rb-1,-1):
                    res.append(matrix[l][cb])
                cb+=1
        return res       
        