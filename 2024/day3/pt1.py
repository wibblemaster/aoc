#!/usr/local/env python
import re


# toparse = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def loadstuff():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    cache = [x.strip() for x in lines]
    return ''.join(cache)

def main():
    toparse = loadstuff()
    x = re.findall(r'mul\(\d+,\d+\)', toparse)
    print(x)
    x = [y.replace('mul(','').replace(')','') for y in x]
    print(x)

    summation = 0
    for i in x:
        elems = i.split(',')
        summation += int(elems[0]) * int(elems[1])

    print(summation)


if __name__ == "__main__":
    main()
