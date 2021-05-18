#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program using nested loop

def main():
    # this function using nested loop
    counter1 = 0
    counter2 = 0
    for counter1 in range(10):
        for counter2 in range(10):
            the_number = counter1 * counter2
            print("{0} X {1} = {2}".format(counter1, counter2, the_number))


if __name__ == "__main__":
    main()
