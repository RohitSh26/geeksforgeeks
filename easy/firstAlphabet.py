# User function Template for python3
class Solution:
    def firstAlphabet(self, S):
        # code here
        output = ''
        for i in S.split(' '):
            if i[0] is not None:
                output += i[0]
        return output

    def firstAlphabet_better(self, S):
        # code here
        take_index = 0
        output = S[take_index]
        for i in range(len(S)):
            
            if S[i] == ' ':
                take_index = i + 1
                output += S[take_index]
        return output

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.firstAlphabet_better(S)

        print(answer)

# } Driver Code Ends