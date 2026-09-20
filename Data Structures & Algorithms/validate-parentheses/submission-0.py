class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []


        for ch in s:
            if ch in closeToOpen:
                if not stack: return False # needs to be a stack, cannot start with )]}
                elif stack[-1] == closeToOpen[ch]: # e.g. stack ends with [ and we saw a ]
                    stack.pop()
                else: return False
            else:
                stack.append(ch)
        
        if stack: return False
        else: return True