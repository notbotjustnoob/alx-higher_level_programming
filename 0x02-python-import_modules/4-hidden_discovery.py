#!/usr/bin/python3.8
import dis

if __name__ == '__main__':
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()

    instructions = dis.get_instructions(code)
    names = set()

    for instruction in instructions:
        if instruction.opname == 'LOAD_NAME':
            name = instruction.argval
            if not name.startswith('__'):
                names.add(name)

    for name in sorted(names):
        print(name)
