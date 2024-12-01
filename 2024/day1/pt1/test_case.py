#!/usr/bin/env python

def main():
    with open("testdata.txt") as f:
        lines = f.readlines()

    data = [x.strip() for x in lines]
    col1 = []
    col2 = []
    for i in data:
        col1.append(int(i.split()[0]))
        col2.append(int(i.split()[1]))

    col1.sort()
    col2.sort()

    summation = 0
    for i in range(len(col1)):
        summation += abs(col1[i] - col2[i])
    print(summation) 

if __name__ == "__main__":
    main()
