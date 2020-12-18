class Grammar:
    def __init__(self, _nonterminal_symbols, _terminal_symbols, _productions, _start_terminal):
        self.nonterminal_symbols = _nonterminal_symbols
        self.terminal_symbols = _terminal_symbols
        self.productions = _productions
        self.start_terminal = _start_terminal

    @staticmethod
    def read_from_file(filename):
        with open(filename) as file:
            nonterminal_symbols = Grammar.parse_line(file.readline())
            terminal_symbols = Grammar.parse_line(file.readline())
            start_terminal = Grammar.parse_line(file.readline())
            productions = Grammar.parse_productions(Grammar.parse_line(''.join([line for line in file])))
        return Grammar(nonterminal_symbols, terminal_symbols, productions, start_terminal)

    @staticmethod
    def parse_line(line):
        return [element.strip() for element in line.strip().split('=')[1].strip()[1:-1].split(',')]

    @staticmethod
    def parse_productions(productions):
        result = []
        for rule in productions:
            [lhs, rhs] = rule.strip().split('->')
            results = rhs.strip().split('|')
            for res in results:
                result.append((lhs.strip(), res.split()))
        return result

    def find_production(self, symbol):
        result = []
        for production in self.productions:
            if production[0] == symbol:
                result.append(production[1])
        return result

    def menu(self):
        print("0 - Exit")
        print("1 - Productions")
        print("2 - Nonterminal symbols")
        print("3 - Terminal symbols")
        print("4 - Productions for a given nonterminal")

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
                print(self.find_production(nt))
