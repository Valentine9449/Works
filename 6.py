#1
a = "hi"
print(a.capitalize())
#2
b = "HELLO"
print(b.casefold())
#3
txt = input("Введите строку: ")
x = txt.center(10, "!")
print(x)
#4
print(txt.count("a"))
#5
print(txt.encode())
#6
print(txt.endswith("k"))
#7
txt2 = "W\to\tr\tl\td"
print(txt2.expandtabs(2))
#8
c = "How are you?"
print(c.find("a"))
#9
example = "Hi, i buy a new {}, its {}".format("car", "VAZ 21099")
print(example)
#10
print(c.index("are"))
#11
example2 = input("Введите строку: ")
print(example2.isalnum())
#12
print(example2.isalpha())
#13
example3 = "\u0033" #unicode for 3
x = example3 .isdecimal()
print(x)
#14
digit = input("Введите строку: ")
print(digit.isdigit())
#15
example4 = "Demo"
x = example4.isidentifier()
print(x)
#16
print(a.islower())
#17
print(a.isnumeric())
#18
print(example2.isprintable(), "\nМожна распечатать")
#19
print(c.isspace())
#20
print(c.istitle())
#21
upper = "ABDSA"
print(upper.isupper())
#22(Join)
print("!".join(upper))
#22(ljust)
x = example4.ljust(20)
print(x,"No Demo")
#23(lower)
print(b.lower())
#24(lstrip)
txt = "     dog     "
x = txt.lstrip()
print("of all animals", x, "is my favorite")
#25(split)
spl = "good weather today"
print(spl.split())
#26(strip)
txt = "     dog     "
x = txt.strip()
print("of all animals", x, "is my favorite")
#27(splitlines)
txt = "of all animals\nis my favorite"
x = txt.splitlines()
print(x)
#28(title)
print(txt.title())
#29(upper)
up = "adasdad"
up1 = up.upper()
print(up1)
#30
mytable = up.maketrans("a", "P")
print(up.translate(mytable))
#31
print(up.partition("d"))
#32(swapcase)
swap = "Hi,my name Is Unknown"
print(swap.swapcase())
#33(zfill)
print(swap.zfill(30))
#34(startwith)
new_line = "Hi world"
print(new_line.startswith("Hi"))
#35(replace)
print(swap.replace("Unknown","Volodya"))
