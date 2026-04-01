class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for i in s:
            if i in char_dict.values():
                stack.append(i)
            elif stack:
                pop = stack.pop()
                if char_dict.get(i) != pop: 
                    return False
            else: return False

        if len(stack) == 0: return True
        else: return False