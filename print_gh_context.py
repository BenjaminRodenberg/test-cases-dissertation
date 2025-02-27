import os

print("Hello World!")

print(os.environ)
print(f"{os.environ['GITHUB_HEAD_REF']}")
print(f"{os.environ['GITHUB_SHA']}")

print("Byebye!")