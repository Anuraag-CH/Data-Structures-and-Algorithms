class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s :
            if i in '({[':
                stack.append(i)
            elif stack == []:
                return False
            elif i == ')' and stack.pop() != '(':
                return False
            elif i == '}' and stack.pop() != '{':
                return False
            elif i == ']' and stack.pop() != '[':
                return False
        
        if stack != [] :
            return False
        
        return True

        