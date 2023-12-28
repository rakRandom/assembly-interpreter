def simple_assembler(code):
    variables = {}
    total_lines = len(code)

    read_header = 0
    while read_header < total_lines:
        cmd, *args = code[read_header].split()

        match cmd:
            case 'mov':
                arg1, arg2 = args
                variables[arg1] = int(arg2) if not arg2.isalpha() else variables[arg2]
                read_header += 1
            case 'inc':
                arg1 = args[0]
                variables[arg1] += 1
                read_header += 1
            case 'dec':
                arg1 = args[0]
                variables[arg1] -= 1
                read_header += 1
            case 'jnz':
                arg1, arg2 = args
                arg1 = variables[arg1] if arg1.isalpha() else int(arg1)
                read_header += int(arg2) if arg1 != 0 else 1

    return variables
