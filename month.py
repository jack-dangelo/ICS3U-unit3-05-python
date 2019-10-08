#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: October 2019
# This program takes user number
# And displays the corresponding month


def main():
    while True:
        # input
        print("Enter a number between 1 - 12")
        number = int(input("1 would be January and 12 would be December: "))

        # process
        if number == 1:
            # output
            print()
            print("January")

        # process
        elif number == 2:
            # output
            print()
            print("Febuary")

        # process
        elif number == 3:
            # output
            print()
            print("March")

        # process
        elif number == 4:
            # output
            print()
            print("April")

        # process
        elif number == 5:
            # output
            print()
            print("May")

        # process
        elif number == 6:
            # output
            print()
            print("June")

        # process
        elif number == 7:
            # output
            print()
            print("July")

        # process
        elif number == 8:
            # output
            print()
            print("August")

        # process
        elif number == 9:
            # output
            print()
            print("September")

        # process
        elif number == 10:
            # output
            print()
            print("October")

        # process
        elif number == 11:
            # output
            print()
            print("November")

        # process
        elif number == 12:
            # output
            print()
            print("December")

        # prevents program from crashing
        if number not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            print()
            print("Please enter a valid number between 1 - 12")
            print()
            continue

        # breaks out of while loop
        else:
            break


if __name__ == "__main__":
    main()
