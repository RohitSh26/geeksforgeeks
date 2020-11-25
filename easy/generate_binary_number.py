#User function Template for python3
'''
Function Arguments :
		@param  : n (given number)
		@return : list of all the binary numbers till n.
'''
def generate(N):
    # code here
    output = []

    from queue import Queue

    q = Queue()

    q.put('1')

    while N > 0:
        N -= 1
        print(q.queue)
        first = q.get()
        
        #1 ->1
        #   ->10, 11
        #10 
        #   ->11, 100, 101 
        #11
        #   ->100, 101, 110, 111
        #100
        #   ->101, 110, 111, 1000, 1001
        #101
        #   ->110, 111, 1000, 1001, 1010, 1011

        output.append(first)
        second = first
        q.put(first + '0')
        q.put(second + '1')
    
    return output

# f = 1 fS 10 fSf 101 fSfS 1010

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by :  Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
    
    # print(generate(N=6))
# } Driver Code Ends