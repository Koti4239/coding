class Solution:
    def rob(self,n):
        return max(n[0],self.helper(n[1:]),self.helper(n[:-1]))
    def helper(self,n):
        rob1=0
        rob2=0
        for i in n:
            tem=max(i+rob1,rob2)
            rob1=rob2
            rob2=tem
        return(rob2)  
n=list(map(int,input().split()))
obj=Solution()
obj.rob(l)
obj.helper(l)
        
