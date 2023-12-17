first = 10
second = 0

if second > 0:
    print(first / second)
else:
    print("division by zero")

# print(first/second)
print("Hello Python")

try:
    print(name)
except:
    print("name is not define")

print("=================================")

try:
    print(first / second)
    print(cat)
except ZeroDivisionError:
    print("division error")
except NameError:
    print("name error")

print("=================================")

try:
    print(cat)
    list_dog = []
    print(first / second)
    print(list_dog[10])
except (ZeroDivisionError, NameError, IndexError) as error:
    print("any error", error)

print("=================================")

try:
    try:
        print(cat)
        list_dog = []
        print(first / second)
        print(list_dog[10])
    except SyntaxError as error:
        print("any error")
except BaseException as error:
    print("base = ", error)

print("=================================")

try:
    list_dog = ["puffy", "bobik", "sharik"]
    print(list_dog[1])
except NameError as error:
    print(error)
else:
    try:
        print(0 / 0)
    except ZeroDivisionError as e:
        print(e)
    print("ELSE!!!!!")
finally:
    print("finally working all time")

print("End program")
