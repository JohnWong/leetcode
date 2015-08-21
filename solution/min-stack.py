class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.data = list()
        self.indicator = list()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)
        count = len(self.indicator)
        if count > 0:
            self.indicator.append(min(self.indicator[count - 1], x))
            pass
        else:
            self.indicator.append(x)
            pass

    # @return nothing
    def pop(self):
        self.data.pop()
        self.indicator.pop()

    # @return an integer
    def top(self):
        return self.data[len(self.data) - 1]
        

    # @return an integer
    def getMin(self):
        return self.indicator[len(self.data) - 1]


if __name__ == '__main__':
    s = MinStack()
    s.push(10)
    print(s.top(), s.getMin())
    s.push(3)
    print(s.top(), s.getMin())
    s.push(2)
    print(s.top(), s.getMin())
    s.push(8)
    print(s.top(), s.getMin())
    s.pop()
    print(s.top(), s.getMin())