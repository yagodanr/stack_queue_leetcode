from queue import LifoQueue

class FreqStack:

    def __init__(self):
        self.s = LifoQueue()
        self.s1 = LifoQueue()


    def push(self, val: int) -> None:

        present = False
        while not self.s.empty():
            st: LifoQueue = self.s.get()
            top = st.pop()
            if top == val:
                st.put(val)
                present = True

            self.s1.put(st)

        if not present:
            tmp = LifoQueue()
            tmp.put(val)
            self.s1.put(tmp)
        self.s, self.s1 = self.s1, self.s



    def pop(self) -> int:



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()