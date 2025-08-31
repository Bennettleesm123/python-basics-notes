
"""
python_basics.py — simple tour of Python basics.
Run: python3 python_basics.py
"""

print("=== 0) Hello Python ===")
print("Hello, world!")

# Variables and types
print("\n=== 1) Variables & types ===")
x = 7
pi = 3.14
flag = True
name = "Bennett"
print(type(x), type(pi), type(flag), type(name))

# Operators
print("\n=== 2) Operators ===")
a, b = 10, 3
print("add:", a+b, "sub:", a-b, "mul:", a*b, "div:", a/b)

# If/else
print("\n=== 3) If/else ===")
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C or below")

# Loops
print("\n=== 4) Loops ===")
for i in range(3):
    print("for loop i:", i)
n=0
while n<3:
    print("while loop n:", n)
    n+=1

# Functions
print("\n=== 5) Functions ===")
def greet(who="world"):
    return f"Hello, {who}!"
print(greet("Atlas"))

# Lists, tuples, sets, dicts
print("\n=== 6) Collections ===")
nums=[1,2,3]; nums.append(4)
print("list:", nums)
coords=(10,20)
print("tuple:", coords)
letters={"a","b","a"}
print("set:", letters)
person={"name":"Bennett","likes":["jazz","bonsai"]}
print("dict:", person)

# Strings
print("\n=== 7) Strings ===")
s="python is fun"
print(s.upper(), "contains 'fun'?", "fun" in s)

# File I/O
print("\n=== 8) File I/O ===")
with open("demo.txt","w") as f: f.write("hi file!")
with open("demo.txt") as f: print(f.read())

# Try/except
print("\n=== 9) try/except ===")
try:
    print(5/0)
except ZeroDivisionError:
    print("cannot divide by zero")

# Imports
print("\n=== 10) Imports ===")
import math
print("sqrt(16)=", math.sqrt(16))

# Tiny class
print("\n=== 11) Class ===")
class Counter:
    def __init__(self):
        self.value=0
    def inc(self):
        self.value+=1
c=Counter()
c.inc(); c.inc()
print("counter value:", c.value)

# Mini exercises
print("\n=== 12) Mini exercises (try yourself) ===")
print("1) Write function double(x) that returns 2*x")
print("2) Return positives from list")
print("3) Count vowels in string")
