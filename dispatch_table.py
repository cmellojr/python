# Calculate how many point a brazilian team has at the end of a tournament 

tournament_teams_victory = {
    "Palmeiras": 10,
    "São Paulo": 7,
    "Corinthians": 6,
    "Santos": 4
}

# In Python, a dispatch table is a common and efficient programming pattern implemented as a dictionary that maps keys
# (such as strings or numbers) to functions or methods. This allows dynamic function calling at runtime, avoiding long
# and less readable if-elif chains, similar to a switch-case in other languages. 
#
# How to Implement a Dispatch Table in Python
#
# Since functions are "first-class citizens" in Python, they can be stored as values in a dictionary just like any
# other object. The basic implementation involves defining functions and then creating a dictionary where the keys 
# correspond to the desired function names. 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# The dispatch table (dictionary of functions)
dispatch_table = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
}

# Usage: retrieve the function by its key and call it
operation = 'add'
result = dispatch_table[operation](10, 5)
print(f"Result of '{operation}': {result}") # Output: Result of 'add': 15

operation = 'subtract'
result = dispatch_table[operation](10, 5)
print(f"Result of '{operation}': {result}") # Output: Result of 'subtract': 5

# Key Advantages

# Readability: The code is cleaner and more readable, as it separates the dispatch logic from the function handlers.

# Performance: Dictionary lookups are generally an O(1) (constant time) operation, which is much faster than the
# O(n) (linear time) required to scan a long chain of if-elif statements.
#
# Flexibility and Maintainability: Functions can be added, removed, or changed by simply modifying the dictionary, 
# without altering the main logic that uses the table.
#
# Dynamic Behavior: It supports late binding, meaning the specific function to be called is determined at runtime
# based on the key. 

# Alternative: functools.singledispatch
# 
# For cases where you want a single function name to behave differently based on the type of the arguments passed
# to it (function overloading), Python provides the built-in @functools.singledispatch decorator in its standard 
# library. 


from functools import singledispatch

@singledispatch
def process(arg, **kwargs):
    print(f"Generic processing for type: {type(arg)}")

@process.register(int)
def _(arg, **kwargs):
    print(f"Processing an integer: {arg}")

@process.register(str)
def _(arg, **kwargs):
    print(f"Processing a string: {arg!r}")

process(10)
process("hello")

