from collections import deque

class FreqStack:

    def __init__(self):
        self.s = deque()
        self.freq = {}
        self.most_freq = 0


    def push(self, val: int) -> None:
        self.s.append(val)
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        self.most_freq = max(self.most_freq, self.freq[val])


    def pop(self) -> int:
        s1 = deque()
        el = None
        while len(self.s):
            el = self.s.pop()
            if self.freq[el] == self.most_freq:
                while len(s1):
                    self.s.append(s1.pop())
                self.freq[el] -= 1
                self.most_freq = max(self.freq.values())
                break
            s1.append(el)
        return el


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