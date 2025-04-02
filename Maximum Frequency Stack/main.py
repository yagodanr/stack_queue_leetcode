from queue import LifoQueue
from collections import deque

class FreqStack:

    def __init__(self):
        self.s = deque()


    def push(self, val: int) -> None:
        self.s.append(val)


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

        s2 = deque()
        while len(self.s):
            val = self.s.popleft()
            search_add(val)
            s2.appendleft(val)
        while len(s2):
            self.s.appendleft(s2.popleft())
        most_freq = tmp.get()
        while not tmp.empty():
            val = tmp.get()
            if val[1] > most_freq[1]:
                most_freq = val
        most_freq = most_freq[0]
        while len(self.s):
            val = self.s.pop()
            if val == most_freq:
                break
            s2.append(val)
        while len(s2):
            self.s.append(s2.pop())
        return most_freq


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# freqStack = FreqStack()
# freqStack.push(5) # The stack is [5]
# freqStack.push(7) # The stack is [5,7]
# freqStack.push(4) # The stack is [5,7,5,7,4]
# print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].

freqStack = FreqStack()
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