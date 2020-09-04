import pytest
import inspect
from test_utils import *
import random
import re
import session4 
from session4 import Qualean
import math
import os
from decimal import Decimal

num = random.choice([-1,0,1])




# def test_fourspace_equal():
#     assert fourspace(session4) == False, 'Not all spaces before lines are a multiple of 4!'

def test_function_names():
    assert function_name_had_cap_letter(session4) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_addition():
    num = random.choice([-1,0,1])
    q = Qualean(num)
    sum_of_q = Qualean(0)
    for i in range(100):
        sum_of_q = q + sum_of_q
#         print(sum_of_q)
#         return sum_of_q
#     return sum_of_q == q*100
#     print(sum_of_q,q*100)
    # return sum_of_q == q *100
    assert sum_of_q == q *100 ,"summing of q 100 times is equal to q multiplied by 100"

def test_or():
    q1 = Qualean(num)
    # return bool(q or p)
    q2 = None
    assert q1 or q2 , "even when the second variable is not defined ,if q is not false then it shouldn't give false"

def test_and():
    q = Qualean(False)
    assert bool(q and p), "even when the second variable is not defined ,if q is  false then it should give false"

    
def test_sqrt():
    q = Qualean(num)
    # print(q.__sqrt__() ,Decimal(q.__float__()))
    assert q.__sqrt__() == Decimal(math.sqrt(q))

# def test_sum_one_million():
#     sum_of_q = 0
#     for i in range(1000000):
#         if i % 2 ==0:
#             num  = 1
#         else :
#             num = -1
#         q = Qualean(num)
#         sum_of_q = q + sum_of_q
# #         print(q, num)
# #         print(sum_of_q)
#     assert math.isclose(sum_of_q,0 ,rel_tol = 0.1,abs_tol = 0.1)
