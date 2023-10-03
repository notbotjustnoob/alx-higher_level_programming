#!/usr/bin/python3
factor = 0
for i in range(122, 96, -1):
    print("{:c}".format(i-32*(i % 2)), end="")
