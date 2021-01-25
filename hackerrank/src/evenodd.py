#!/bin/python

import math
import os
import random
import re
import sys


def is_odd(num):
    is_even = num % 2 == 0
    if is_even:
        if 2 <= num <= 5:
            print("Not Weird")
        elif 6 <= num <= 20:
            print("Weird")
        elif num > 20:
            print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    n = int(input().strip())
    is_odd(n)
