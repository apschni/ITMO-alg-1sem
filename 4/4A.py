class Stack:
    def __init__(self):
        self.stack = []
    def push(self,elem):
        self.stack += [elem]
    def pop(self):
        self.stack = self.stack[0:-1]


f = open('stack.in', 'r')
stack = Stack()
n = int(f.readline())
fout = open('stack.out', 'w')
for i in range(n):
    stackin = f.readline().split()
    sign = stackin[0]
    if sign == "+":
        stack.push(stackin[1])
    else:
        print(stack.stack[-1], file=fout)
        stack.pop()
