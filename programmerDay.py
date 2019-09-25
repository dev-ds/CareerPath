# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:18:18 2019

@author: inkdhakshn
"""

# sum up days upto August

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import date

leapYearDays = 31 + 29 + 31 + 30 + 31 + 30 + 31 +31
NonLearYearDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 +31
year1918 = 31 + 15 + 31 + 30 + 31 + 30 + 31 +31

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year > 1918:
        if (year%400 == 0) or (year%4 == 0 and year % 100 != 0):
            diff = 256 - leapYearDays
        else:
            diff = 256 - NonLearYearDays
    elif year < 1918:
        if year%4 == 0:
            diff = 256 - leapYearDays
        else:
            diff = 256 - NonLearYearDays
    else:
        diff = 256 - year1918
        
    d = date(year, 9, diff)
    return str(d.strftime('%d.%m.%Y'))

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result + '\n')