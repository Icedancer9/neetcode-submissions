class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.getMin(), val)))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][-1]



# for every push we do, we store it as (curr_val, curr_min_val_in_stack).
# This way, whenever we pop a value, we are not losing the min value when we pop the min_val, because all the elements in the stack have a record of what the min_value WAS UP TO THEIR POINT. WE ARE MAKING SURE THEY HAVE MEMORY OF THE MIN VALUE THEY HAVE SEEN SO FAR. 
        
