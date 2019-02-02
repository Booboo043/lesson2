class Stack():

    def __init__(self):
        self.items = [] # Initialize a list

    def is_empty(self):
        # Returns True if it is empty, otherwise returns False
        return self.items == []

    def pop(self):
        try:
            return self.items.pop()
        except:
            raise

    def push(self, item):
        self.items.append(item)

    def peek(self):
        # Return to the top of the stack
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)