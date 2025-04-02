import queue

class MyStack:

    def __init__(self):
        self.q = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x: int) -> None:
        # self.q2.put(x)
        # while not self.q.empty():
        #     self.q2.put(self.q.get())

        # self.q, self.q2 = self.q2, self.q

        self.q.put(x)

    def pop(self) -> int:
        if self.q.empty():
            return None

        prev = None
        while True:
            prev = self.q.get()
            if self.q.empty():
                self.q, self.q2 = self.q2, self.q
                return prev
            self.q2.put(prev)



    def top(self) -> int:
        prev = None
        while not self.q.empty():
            prev = self.q.get()
            self.q2.put(prev)

        self.q, self.q2 = self.q2, self.q
        return prev


    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())