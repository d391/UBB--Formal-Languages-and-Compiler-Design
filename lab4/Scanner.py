import re
from SymTabRedo import SymTab
class Scanner:
    def __init__(self):
        self.tokens = {}
        self.readTokens()
        self.ST = SymTab(10)

    def readTokens(self):
        f = open("tokens.in", "r")
        for line in f:
            tok = line.split(" ")
            self.tokens[tok[0]] = int(tok[1].strip("\n"))

        f.close()

    def detectToken(self, line):
        tokens = line.split()
        return tokens

    def verifyReserved(self, token):
        return token in self.tokens.keys()

    def verifyID(self, token):
       return token.isalpha()

    def verifyConst(self, token):
        try:
            if token != '+0' and token != '-0':
                x = int(token)
                return True
        except:
            if token[0] == "\"" and token[-1] == "\"":
                return self.verifyID(token.strip("\""))
        return False

    def pos(self, token):
        try:
            index = self.ST.get(token)
        except:
            index = self.ST.add(token, token)
        return index

    def scan(self):
        foundErr = False
        lineNr = 1
        programFile = open("error.txt", "r")
        pifFile = open("PIF.out", "w")
        for line in programFile:
            lineTokens = self.detectToken(line)
            for t in lineTokens:
                t = t.strip(";:, ()")
                if self.verifyReserved(t):
                    pifFile.write(str(t) + " 0\n")
                elif self.verifyID(t) or self.verifyConst(t):
                    index = self.pos(t)
                    pifFile.write(t + " " + str(index) + "\n")
                else:
                    print("Lexical error " + t + " at line number " + str(lineNr))
                    foundErr = True
            lineNr += 1

        if foundErr is False:
            print("Lexically corect!")

        STfile = open("ST.out", "w")
        STfile.write(str(self.ST))

        STfile.close()
        programFile.close()
        pifFile.close()


if __name__ == "__main__":
    s = Scanner()
    s.scan()
