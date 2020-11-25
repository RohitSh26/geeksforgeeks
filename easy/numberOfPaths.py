#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        

        if m == 1 or n == 1:
            print(m, n)
            return 1

        return self.numberOfPaths(n - 1, m) + self.numberOfPaths(n, m - 1)




#{ 
#  Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    # ob = Solution()
    # t = int (input ())
    # for _ in range (t):
    #     m, n = map(int, input().split())
    #     ans = ob.numberOfPaths(m, n)
    #     print(ans)

    ob = Solution()
    print(ob.numberOfPaths(3, 3))


# } Driver Code Ends