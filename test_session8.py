import pytest
import random
import string
import os
import inspect
import re
import math
import session8 


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding = "utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = "utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    print(spaces)
    for space in spaces:
        print(space)
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_Doc_string_length():
    fn = session8.loc_length()
    assert fn(sum) == 'Function sum docstring length is more then 50 characters'
    assert fn(abs) == 'Function abs docstring length is less then 50 characters'


def test_fibonacci_number():
    fn = session8.fibonacci_number()
    assert fn() == 'First number in fibonacci series is 0'
    assert fn() == 'Second number in fibonacci series is 1'
    assert fn() == 'Next number in fibonacci series is 1'
    assert fn() == 'Next number in fibonacci series is 2'
    assert fn() == 'Next number in fibonacci series is 3'
    assert fn() == 'Next number in fibonacci series is 5'
    assert fn() == 'Next number in fibonacci series is 8'
    assert fn() == 'Next number in fibonacci series is 13'
    assert fn() == 'Next number in fibonacci series is 21'
    
def add(a, b):
    return a + b
def mul(a, b):
    return a*b
def div (a , b):
    if b !=0:
        return(a/b)
    else:
        return(None)
    
def test_counter():
    counter_add = session8.counter(add)
    counter_mul = session8.counter(mul)
    counter_div = session8.counter(div)
    counter_add(1, 2)
    counter_add(3, 4)
    counter_add(6, 5)
    assert session8.func_dict == {'add' : 3 , 'mul' : 0 , 'div' : 0 }
    counter_mul(20,2)
    counter_mul(40,3)
    counter_mul(100,6)
    assert session8.func_dict == {'add' : 3 , 'mul' : 3 , 'div' : 0 }
    counter_mul(13,2)
    counter_mul(2,5)
    assert session8.func_dict == {'add' : 3 , 'mul' : 5 , 'div' : 0 }
    counter_div(100,18)
    assert session8.func_dict == {'add' : 3 , 'mul' : 5 , 'div' : 1 }
    
    
times_dict1 = {'add' : 0 , 'mul' : 0 , 'div' : 0 }
times_dict2 = {'add' : 0 , 'mul' : 0 , 'div' : 0 }

def test_counter2():   
    counter_times_dict1 = session8.counter_dict(times_dict1)
    counter_times_dict1(add,1, 2)
    counter_times_dict1(add,10, 20)
    counter_times_dict1(mul,1, 2)
    counter_times_dict1(mul,10, 20)
    counter_times_dict1(mul,3, 2)
    counter_times_dict1(div,1, 2)
    counter_times_dict1(div,4, 10)
    counter_times_dict1(div,100, 2)
    assert times_dict1 == {'add' : 2 , 'mul' : 3 , 'div' : 3 }
    
    counter_times_dict2 = session8.counter_dict(times_dict2)
    counter_times_dict2(add,1, 2)
    counter_times_dict2(mul,10, 20)
    counter_times_dict2(mul,1, 2)
    counter_times_dict2(mul,10, 20)
    counter_times_dict2(mul,3, 2)
    counter_times_dict2(mul,1, 2)
    counter_times_dict2(div,4, 10)
    counter_times_dict2(div,100, 2)
    assert times_dict2 == {'add' : 1 , 'mul' : 5 , 'div' : 2 }
