class Stack:
    def __init__(self):
        self.stack = []
    def push(self,elem):
        self.stack += [elem]
    def pop(self):
        self.stack = self.stack[0:-1]



f = open('brackets.in', 'r')
stack = Stack()

fout = open('brackets.out', 'w')
stackin = f.read().split()

for elem in stackin:
    stack = Stack()
    fl = 0

    for j in range(len(elem)):
        bracket = elem[j]
        if len(stack.stack)==0 and (bracket in ")]"):
            fl = 1
        else:
            if fl == 0:
                if bracket in "([":
                    stack.push(bracket)
                else:
                    if (bracket == ")" and stack.stack[-1] == "[") or (bracket == "]" and stack.stack[-1] == "("):
                        fl = 1
                    else:
                        stack.pop()
    if fl == 1 or len(stack.stack)!=0:
        print("NO",file = fout)
    else:
        print("YES",file = fout)
    stackin = f.readline()

