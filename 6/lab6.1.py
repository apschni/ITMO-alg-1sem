def hash_function(self, value):
    return value % self.size


class HashTable:
    def __init__(self, size=503049):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def put(self, data):
        if not self.exist(data):
            self.table[self.hsh(data)].append(data)

    def exist(self, data):
        return data in self.table[self.hsh(data)]

    def delete_element(self, data):
        if data in self.table[self.hsh(data)]:
            self.table[self.hsh(data)].remove(data)
        else:
            return


file = open("set.in", "r")
fileo = open("set.out", "w")

HashTable.hsh = hash_function

line = file.readline()
h = HashTable()

while line != "":
    if line[0] == "i":
        h.put(int(line[7:-1]))
    elif line[0] == "e":
        if h.exist(int(line[7:-1])):
            print('true', file=fileo)
        else:
            print('false', file=fileo)
    else:
        h.delete_element(int(line[7:-1]))
    line = file.readline()

fileo.close()