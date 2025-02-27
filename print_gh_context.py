import os

print("Hello World!")

print(os.environ)
print(f"{os.environ['MY_HEAD_REF']}")
print(f"{os.environ['MY_SHA']}")

print("Byebye!")