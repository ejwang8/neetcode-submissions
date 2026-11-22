class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # read Hint 1+2
        stack = []
        operands = ['+', '-', '*', '/']
        for token in tokens:
            if token in operands:
                num2 = int(stack.pop())
                result = int(stack.pop())
                # print(result, token, num2)
                if token == '+':
                    result += num2
                elif token == '*':
                    result *= num2
                elif token == '/':
                    result /= num2
                else:
                    result -= num2
                stack.append(result)
                # print(stack, result)
            else:
                stack.append(token)
                # print('num', token)
                # print(stack)
        return int(stack.pop())
