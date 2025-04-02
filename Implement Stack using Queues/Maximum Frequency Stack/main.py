from queue import LifoQueue

class FreqStack:

    def __init__(self):
        self.s = LifoQueue()


    def push(self, val: int) -> None:
        self.s.put(val)


    def pop(self) -> int:
        tmp = LifoQueue()
        tmp2 = LifoQueue()

        def search_add(val):
            nonlocal tmp, tmp2
            while not tmp.empty():
                top = tmp.get()
                if top[0] == val:
                    while not tmp2.empty():
                        tmp.put(tmp2.get())
                    tmp.put((val, top[1]+1))
                    break
                tmp2.put(top)
            else:
                while not tmp2.empty():
                    tmp.put(tmp2.get())
                    tmp.put((val, 1))

        s2 = LifoQueue()
        while not self.s.empty():
            val = self.s.get()
            search_add(val)
            s2.put(val)
        while not s2.empty():
            self.s.put(s2.get())
        return tmp.get()[0]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

freqStack = FreqStack();
freqStack.push(5) # The stack is [5]
freqStack.push(7) # The stack is [5,7]
freqStack.push(5) # The stack is [5,7,5]
freqStack.push(7) # The stack is [5,7,5,7]
freqStack.push(4) # The stack is [5,7,5,7,4]
freqStack.push(5) # The stack is [5,7,5,7,4,5]
print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
print(freqStack.pop())   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
print(freqStack.pop())   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].