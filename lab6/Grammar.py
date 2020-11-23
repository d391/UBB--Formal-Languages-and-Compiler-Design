class Grammar:
    def __init__(self):
        self.nonterminal_symbols = []
        self.terminal_symbols = []
        self.productions = []
        self.readFromFile()

    def readFromFile(self):
        file = open("g1.txt", "r")
        file.readline()
        line = file.readline()
        while line != "Nonterminal symbols:\n":
            tokens = line.strip('\n').split(" -> ")
            self.productions.append(tokens)
            line = file.readline()
        line = file.readline()
        self.nonterminal_symbols = line.strip("\n").split(" ")
        file.readline()
        line = file.readline()
        self.terminal_symbols = line.strip("\n").split(" ")

    def menu(self):
        print("0 - exit")
        print("1 - Productions")
        print("2 - Nonterminal symbols")
        print("3 - Terminal symbols")
        print("4 - Productions for a given nonterminal")

    def findProductions(self, nt):
        resultProds = []
        for prod in self.productions:
            if nt is prod[0]:
                resultProds.append(prod[1])
        return resultProds


    def printMenu(self):
        while True:
            self.menu()
            choice = int(input("> "))
            if choice == 0:
                return
            if choice == 1:
                print(self.productions)
            if choice == 2:
                print(self.nonterminal_symbols)
            if choice == 3:
                print(self.terminal_symbols)
            if choice == 4:
                nt = input("Give nonterminal: ")
                print(self.findProductions(nt))


if __name__ == "__main__":
    g = Grammar()
    g.printMenu()
