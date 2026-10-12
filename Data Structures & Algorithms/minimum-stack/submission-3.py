class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if value <= self.min_stack[-1]:
            self.min_stack.append(value)
        return None

    
    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val == self.min_stack[-1]:
            self.min_stack.pop() 
            if not self.min_stack and self.stack:
                self.min_stack.append(self.stack[-1])
        
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
    # Main scenario: You have multiple of the same mins. [1 1 2 1] -> pop() -> [1 1 2] but 1 is still the min. We know that because 1 is still in the stack. How do we keep track of this in O(1) time? Use a min_stack

# [2 3 4 5]
# [2]





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()