#!/usr/bin/env python3

# Created By: Patrice Pat-Odita
# Created on: Dec 21, 2022
# This program Generates 10 random numbers, loops it to find the one with
# the greatest value and displays it.

import random

# Generates 10 random numbers
def find_max_value(array_of_nums):
    # This is the variable that will hold the highest value
    max_num = array_of_nums[0]

    for counter in range(len(array_of_nums)):
        current_num = array_of_nums[counter]
        # sets max_num to the current number generated comparing it
        # to see if it is greater than the number.
        if max_num < current_num:
            max_num = current_num
    # Returns the maximum number
    return max_num


def main():

    # declaring variable
    counter = 0
    max_num_arr = []

    # display opening message to console
    print("")
    print(
        "\033[1;35;38mThis program generates a list of random "
        "numbers between 0 and 100, then determines the largest number."
    )
    print("")

    # generates random numbers
    for counter in range(10):

        # putting the random number into the array
        max_num_arr.append(random.randint(0, 100))

        print(
            " {} is added to the list at "
            "position {}".format(max_num_arr[counter], counter)
        )

    # calls the function
    max_value = find_max_value(max_num_arr)

    # displays results
    print("\nThe max value is {}".format(max_value))


if __name__ == "__main__":
    main()
