
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

"""
txt = "You scored {:%}"
print(txt.format(0.25))
txt = "You scored {:.0%}"
print(txt.format(0.25))
"""

"""myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
"""

"""txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
"""

"""txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
"""

"""txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
"""

"""txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
"""

"""
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
"""

"""txt = "Mi casa, sua casa."
x = txt.rindex("casa")
print(x)
"""

"""txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit")
"""

"""txt = "I could eat bananas all day, bananas are my favorite fruit."
x = txt.rpartition("bananas")
print(x)

"""
"""txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
"""

"""
txt = "bananas,,,,,,,,,,ssssqqqw......"
x = txt.rstrip(",.qsw")
print(x)
"""

"""
txt = "welcome to the jungle"
x = txt.split()
print(x)
"""

"""txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
"""
"""
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
"""

"""txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)
"""

"""txt = "         banana          "
x = txt.strip()
print("of all fruits", x, "is my favorite")
"""

"""txt = ",,,,,,,,,,,,rrttgg......banana.....rrrr"
x = txt.strip(",.grt")
print(x)
"""

"""txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
"""


"""txt = "Welcome to my world"
txt = "Welcome to my 2nd world"
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)
"""

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
"""
mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict))
"""

"""
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
"""

"""txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))
"""

"""
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))
"""

"""
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111,111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
"""

"""
txt = "Hello my friends"
x = txt.upper()
print(x)
"""

"""
txt = "50"
x = txt.zfill(10)
print(x)
"""

"""
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
"""











