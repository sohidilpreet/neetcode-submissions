class Solution:
    def isopening(self, first):
        match first:
            case '(':
                return True
            case '{':
                return True
            case '[':
                return True
        return False

    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        for char in s:
            if self.isopening(char):
                stack.append(char)
            else:
                if not stack or not self.isvalidpair(stack.pop(), char):
                    return False
        if stack:
            return False
        return True
    
    def isvalidpair(self, first, second):
        if first == '(' and second == ')':
            return True
        if first == '[' and second == ']':
            return True
        if first == '{' and second == '}':
            return True
        return False