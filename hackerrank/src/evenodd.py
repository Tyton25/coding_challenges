#!/bin/python

import math
import os
import random
import re
import sys


def is_odd(num):
    if num % 2 != 0:
        print("Weird")


if __name__ == '__main__':
    n = int(input().strip())
    is_odd(n)
