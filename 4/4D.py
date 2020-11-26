class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,elem):
        self.stack += [elem]
    def pop(self):
        last = self.stack[-1:]
        self.stack = self.stack[0:-1]
        return last


f = open('postfix.in', 'r')
stack = Stack()

fout = open('postfix.out', 'w')
fl = 0
stackin = f.readline().split()

for elem in stackin:
    if elem == "+":
        b = int(stack.pop()[0])
        a = int(stack.pop()[0])
        stack.push(a + b)

    elif elem == "-":
        b = int(stack.pop()[0])
        a = int(stack.pop()[0])
        stack.push(a - b)

    elif elem == "*":
        b = int(stack.pop()[0])
        a = int(stack.pop()[0])
        stack.push(a * b)

    else:
        stack.push(int(elem))

print(stack.pop()[0], file=fout)
