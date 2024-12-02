#!/usr/bin/env python

def main():
    # with open("testdata.txt", "r") as f:
    with open("data.txt", "r") as f:
        lines = f.readlines()

    data = [x.strip() for x in lines]
    count = 0
    for l in data:
        r = [int(x) for x in l.split()]
        if r[0] > r[1] and ((r[0] - r[1]) < 4):
            count += decreasing(r)
        elif r[0] < r[1] and ((r[1] - r[0]) < 4):
            count += increasing(r)
    print(data)
    print(count)

def increasing(r):
    for i in range(1, len(r)-1):
        if r[i] == r[i+1]:
            return 0
        elif r[i] > r[i+1]:
            return 0
        elif (r[i+1] - r[i]) > 4:
            return 0
    return 1

def decreasing(r):
    for i in range(1, len(r)-1):
        if r[i] == r[i+1]:
            return 0
        elif r[i] < r[i+1]:
            return 0
        elif (r[i] - r[i+1]) > 4:
            return 0
    return 1

if __name__ == "__main__":
    main()
