#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argz = sys.argv[1:]
    argc = len(argz)
    print("argc = {:d} and op = {:s}".format(argc, argz[1]))
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argz[0])
    op = argz[1]
    b = int(argz[2])
    res = 0

    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == '/':
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {:s} {:d} {:d}".format(a, op, b, res))
