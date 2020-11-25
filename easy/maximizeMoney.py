#User function Template for python3

class Solution:
    def maximizeMoney(self, N , K):
        # code here 
        max_money = 0
        if 1 <= N and K <= pow(10, 3):
            for i in range(N):
                if(i % 2 == 0):
                    max_money += K
        
        return max_money



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = map(int,input().split())
        
        ob = Solution()
        print(ob.maximizeMoney(N,K))
# } Driver Code Ends