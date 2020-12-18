class ParserOutput:
    def __init__(self, _parser):
        self.parser = _parser

    def DS(self, outputParser):
        res = []
        for el in outputParser:
            res.append(self.parser.grammar.productions[el])

        return res

    def writeOutput(self, outputParser, filename):
        for el in self.DS(outputParser):
            filename.write(str(el) + "\n")
