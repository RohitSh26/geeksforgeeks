
class Soluion:
    def isValid(self, s):

        par_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for item in s:
            if(item in par_map.values()):
                stack.append(item)

            else:
                top = stack[-1] if stack else '$'
                print(top)
                if top != par_map[item]:
                    return False    
                stack.pop()

        return not stack

solve = Soluion()
print(solve.isValid("]"))