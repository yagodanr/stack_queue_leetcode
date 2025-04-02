import queue

class MyQueue:

    def __init__(self):
        self.sti = queue.LifoQueue()
        self.sto = queue.LifoQueue()

    def push(self, x: int) -> None:
        if self.sti.empty():
            while not self.sto.empty():
                self.sti.put(self.sto.get())

        self.sti.put(x)

    def pop(self) -> int:
        if self.sto.empty():
            while not self.sti.empty():
                self.sto.put(self.sti.get())

        return self.sto.get()


    def peek(self) -> int:
        if self.sto.empty():
            while not self.sti.empty():
                self.sto.put(self.sti.get())

        tmp = self.sto.get()
        self.sto.put(tmp)
        return tmp


    def empty(self) -> bool:
        return self.sto.empty() and self.sti.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()