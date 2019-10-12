# -*- coding: utf-8 -*-
import sys

lists = [7, "Cauchy", 3.14, "5", 0]

for x in lists:
    try:
        print("Number: " + str(x))
        result = 1/int(x)
        print("Result: ", str(result))
    except:
        print(str(x) + " could not calculated!")
        print("Error type: ", sys.exc_info()[0]) # tyoe of the exception
    finally:
        print("Operations finished!")