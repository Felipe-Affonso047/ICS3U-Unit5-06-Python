#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program rounds decimals

import math


def decimal_rounding(numbers):
    # this function rounds decimals
    rounding_float = float((numbers[0] * pow(10, numbers[1])) + 0.5)
    rounding_int = int(rounding_float)
    rounded_number = rounding_int / pow(10, numbers[1])
    numbers[0] = rounded_number


def main():
    # Is the main function
    try:
        number = float(input("Enter a decimal that you want to round: "))
        decimals = int(input("Enter how many decimal places you want: "))

        inputs = []
        inputs.append(number)
        inputs.append(decimals)

        decimal_rounding(inputs)

        print("\n{}".format(inputs[0]))
    except Exception:
        print("\nThis input is invalid, please, insert a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
