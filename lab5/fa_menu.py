class FAmenu:
    def __init__(self):
        self.states = []
        self.initialState = ""
        self.finalStates = []
        self.alphabet = []
        self.transitions = {}
        self.seq = []
        self.readFA()

    def readFA(self):
        fafile = open("fa.in", "r")
        fafile.readline()

        line = fafile.readline()
        while line != "Initial state:\n":
            self.states.append(line.strip("\n"))
            line = fafile.readline()
        self.initialState = fafile.readline().strip('\n')
        fafile.readline()

        line = fafile.readline()
        while line != "Alphabet:\n":
            self.finalStates.append(line.strip("\n"))
            line = fafile.readline()

        line = fafile.readline()
        while line != "Transitions:\n":
            self.alphabet.append(line.strip("\n"))
            line = fafile.readline()

        line = fafile.readline()
        while line != "Sequence:\n":
            tokens = line.split()
            self.transitions[(tokens[0], tokens[1])] = tokens[2]
            line = fafile.readline()

        self.seq = fafile.readline().split()

    def printMenu(self):
        print("0 - to exit")
        print("1 - states")
        print("2 - alphabet")
        print("3 - final states")
        print("4 - transitions")
        print("5 - verify sequence")

    def getState(self, token):
        return token.strip("()").split(',')[0]

    def verifySeq(self):
        state = self.initialState
        while len(self.seq) > 0:
            transition = (state, self.seq.pop(0))
            if transition in self.transitions.keys():
                state = self.transitions[transition]
            else:
                return False
        return state in self.finalStates


    def menu(self):
        while 1:
            self.printMenu()
            choice = int(input("> "))
            if choice == 0:
                return
            if choice == 1:
                print(self.states)
            if choice == 2:
                print(self.alphabet)
            if choice == 3:
                print(self.finalStates)
            if choice == 4:
                print(self.transitions)
            if choice == 5:
                print(self.seq)
                if self.verifySeq():
                    print("The sequence is verified")
                else:
                    print("The sequence is NOT verified")


if __name__ == "__main__":
    m = FAmenu()
    m.menu()
