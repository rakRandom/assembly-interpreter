from modules.interpreter import simple_assembler

if __name__ == '__main__':
    code: list[str] = list()
    line: str = ""

    print("> Assembly Interpreter:")

    while True:
        line = input("> ")
        if line != "" and line != "exit":
            code.append(line)
        else:
            break

    print(simple_assembler(code))
