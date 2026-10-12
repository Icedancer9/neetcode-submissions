class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda x,y: x + y,
            "-": lambda x,y: y - x,
            "*": lambda x,y: x * y,
            "/": lambda x,y: int(y / x)
        }
        for val in tokens:
            if val not in operations:
                stack.append(int(val))
            else:
                operation = operations[val]
                x = stack.pop()
                y = stack.pop()
                stack.append(operation(x, y))
        return stack[-1]

        