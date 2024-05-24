
"""
age = 36
txt = f"My name is John, I am {age}"

print(txt)

"""

"""
price = 59
txt = f"The price is {price} dollars"
print(txt)

"""

"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

"""

"""
txt = f"The price is {20 * 59} dollars"
print(txt)

"""

#Python - Escape Characters

"""
txt = "We are the so-called \"Vikings\"from the north."
print(txt)

"""

"""
txt = 'It\'s alright'
print(txt)
"""

"""
txt = "This will insert one \\ (backslash)."
"""

"""
txt = "Hello\nWorld!
"""

"""
txt = "Hello\rWorld!"
"""

"""
txt = "Hello\tWorld!"
"""

#Python String capitalize() Method

"""
txt = "hello, and welcome to my world."
x = txt.capitalize()

txt = "36 is my age."


txt = "python Is FUN!"

x = txt.capitalize()
print(x)

"""

"""
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
"""
"""
txt = "banana"
x = txt.center(20)
x = txt.center(20, "o")
print(x)
"""
"""
txt = "I love apples, are my favorite fruit"

#x = txt.count("apple")
x = txt.count("apple", 10, 24)

print(x)
"""

"""
txt = "My name is Stále"
x = txt.encode()
print(x)
"""

"""
txt = "Hello, welcome to my world."
x = txt.endswith(".")
x = txt.endswith("my world.", 5, 11)
print(x)
"""

"""
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)
"""

"""
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
"""

"""
txt = "Hello, welcome to my world."
x = txt.find("welcome")
x = txt.find("e")
print(x)
"""

"""
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
"""

"""
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)
"""

"""
txt = "My name is {fname}, I'm {age}".format(fname = "John", age = 26)
txt = "My name is {0}, I'm {1}".format("John", 36)
txt = "My name is {}, I'm {}".format("John", 26)
print(txt)
"""

"""
txt = "We have {:<8} chickens."
txt = "We have {:>8} chickens."
txt = "We have {:^8} chickens."
print(txt.format(49))
"""

"""
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
"""

"""
txt = "The temperature is between {:+} and {:+} degrees celsius."
txt = "The temperature is between {:-} and {:-} degrees celsius."
txt = "The temperature is between {: } and {: } degrees celsius."

print(txt.format(-3, 7))
"""

"""
txt = "The universe is {:,} years old."
txt = "The universe is {:_} years old."

print(txt.format(138000000))

"""

"""
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
"""

"""
txt = "We have {:d} chickens."
print(txt.format(0b101))
"""

"""
txt = "We have {:e} chickens."
txt = "We have {:E} chickens."
print(txt.format(5))
"""

"""
txt = "The price is {:.2f} dollars."
print(txt.format(45))
txt = "The price is {:f} dollars."
print(txt.format(45))

"""

"""
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

"""
"""
txt = "The Hexadecimal version of {0} is {0:x}"
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

"""

txt = "You scored {:%}"
print(txt.format(0.25))
txt = "You scored {:.0%}"
print(txt.format(0.25))
