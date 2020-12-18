from Parser import Parser
from ParserOutput import ParserOutput


class Main:

    def main(self):
        parser = Parser()
        output_parser = parser.parse('aabb')

        parserOutput = ParserOutput(parser)
        print("Derivation strings: " + str(parserOutput.DS(output_parser)))
        outputfile = open("out1.txt", "w")
        parserOutput.writeOutput(output_parser, outputfile)


if __name__ == "__main__":
    main = Main()
    try:
        main.main()
    except Exception as e:
        print(e)
