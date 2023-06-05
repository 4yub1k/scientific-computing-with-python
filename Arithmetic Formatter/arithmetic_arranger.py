def arithmetic_arranger(arith_values=None, result=False):
    if len(arith_values) > 5:
        return "Error: Too many problems."

    new_equations = [equation.split() for equation in arith_values]

    # Yes you add all strings in single variable, but this is just for understanding. no eval().
    equa_1, equa_2, dashes, output = '', "\n", "\n", "\n"

    for e1, sym, e2 in new_equations:  # 1 + 3 : 1 is e1, + is sym, 3 is e2.
        if e1.isnumeric() and e2.isnumeric():
            if len(e1) <= 4 and len(e2) <= 4:
                if sym in ['+', '-']:
                    spaces = len(e1) if len(e1) > len(e2) else len(e2)
                    equa_1 += f"{e1.rjust(spaces + 2)}{' ' * 4}"
                    equa_2 += f"{sym} {e2.rjust(spaces)}{' ' * 4}"
                    dashes += f"{'-' * (spaces + 2)}{' ' * 4}"
                    output += f"{str(int(e1) + int(e2) if sym == '+' else int(e1) - int(e2)).rjust(spaces + 2)}{' ' * 4}"
                else:
                    return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Numbers must only contain digits."
    return f"{equa_1[:-4]}{equa_2[:-4]}{dashes[:-4]}{output[:-4] if result else ''}"
