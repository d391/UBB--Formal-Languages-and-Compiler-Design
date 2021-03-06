class SymTab(object):
    def __init__(self, length):
        self.length = length
        self.array = [None] * length

    def hash(self, key):
        return hash(key) % self.length

    def add(self, key, value):
        if self.verifyFull():
            self.rehash()
        else:
            index = self.hash(key)
            if self.array[index] is not None:
                for pair in self.array[index]:
                    if pair[0] == key:
                        pair[1] = value
                        break
                else:
                    self.array[index].append([key, value])
            else:
                self.array[index] = []
                self.array[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for pair in self.array[index]:
                if pair[0] == key:
                    return pair[1]

            raise KeyError()

    def verifyFull(self):
        pairs = 0
        for pair in self.array:
            if pair is not None:
                pairs += 1

        return pairs > len(self.array)/2

    def rehash(self):
        st2 = SymTab(self.length*2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            for pair in self.array[i]:
                st2.add(pair[0], pair[1])
        self.array = st2.array

    def __str__(self):
        s = ""
        for i in range(self.length):
            if self.array[i] is not None:
                s += str(i) + ": "
                for pair in self.array[i]:
                    s += "(" + str(pair[0]) + ", " + str(pair[1]) + ") "
                s += "\n"
        return s


if __name__ == "__main__":
    st = SymTab(10)
    st.add("a", 1)
    st.add("b", 2)
    st.add("c", 3)
    print(st)
