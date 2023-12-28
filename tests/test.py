from modules.interpreter import simple_assembler


def test(func_return, expectation):
    return func_return == expectation


if __name__ == '__main__':
    results = list()

    code1 = """mov a 5
              inc a
              dec a
              dec a
              jnz a -1
              inc a""".split('\n')

    code2 = """mov c 12
               mov b 0
               mov a 200
               dec a
               inc b
               jnz a -2
               dec c
               mov a b
               jnz c -5
               jnz 0 1
               mov c a""".split('\n')

    results.append(test(simple_assembler(code1), {'a': 1}))
    results.append(test(simple_assembler(code2), {'a': 409600, 'c': 409600, 'b': 409600}))

    if all(results):
        print("success")
