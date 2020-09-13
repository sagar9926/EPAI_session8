# Created By : Sagar Agrawal

# EPAI : Session 7

### Question 1 : Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable

```

def loc_length():
    """ This is en exemple of closure that takes a function and then check whether the function 
passed has a docstring with more than 50 characters. 50 is stored as a free variable"""
    min_length = 50
    def lenght_comparison(fn):
        if (len(fn.__doc__) > min_length):
            return(f"Function {fn.__name__} docstring length is more then 50 characters")
        else:
            return(f"Function {fn.__name__} docstring length is less then 50 characters")
    return(lenght_comparison)

```

### Question 2 : Write a closure that gives you the next Fibonacci number

```

def fibonacci_number():
    """ This function gives you the next Fibonacci number"""
    a = 0
    b = 1
    counter = 1
    def fib_calculator():
        nonlocal a
        nonlocal b
        nonlocal counter
        if counter == 1:
            out = (f"First number in fibonacci series is {a}")
        elif counter == 2:
            out = (f"Second number in fibonacci series is {b}")
        else:
            out = (f"Next number in fibonacci series is {a + b}")
            a , b = b , a+b 
        counter += 1
        return(out)
    return(fib_calculator)

```

### Question 3 : Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts


```

func_dict = {'add' : 0 , 'mul' : 0 , 'div' : 0 }

def counter(fn):
    """ This function can keep a track of how many times add/mul/div functions were called,
    and update a global dictionary variable with the counts"""
    def inner(*args, **kwargs):
        global func_dict
        func_dict[fn.__name__] += 1
        print('{0} has been called {1} times'.format(fn.__name__, func_dict[fn.__name__]))
        return fn(*args, **kwargs)
    return inner  

```

### Question 4 : Modify above such that now we can pass in different dictionary variables to update different dictionaries

```

def counter_dict(times_dict):
    """ This function can keep a track of how many times add/mul/div functions were called,
    and update a dictionary , specific to a user, with the counts"""
    def inner(fn,*args, **kwargs):
        nonlocal times_dict
        times_dict[fn.__name__] += 1
        print('{0} has been called {1} times'.format(fn.__name__, times_dict[fn.__name__]))
        print(times_dict)
        return fn(*args, **kwargs)
    return inner
```

