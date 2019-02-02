class Queue():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # 从队尾插入
        self.items.insert(0, item)

    def dequeue(self):
        try:
            # 从队首弹出
            return self.items.pop()
        except:
            raise

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)