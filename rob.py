class Solution:
    def rob(self,n):
        rob1=0
        rob2=0
        for i in n:
            tem=max(i+rob1,rob2)
            rob1=rob2
            rob2=tem
        return(rob2)    
l=list(map(int,input().split()))
obj=Solution(l)
