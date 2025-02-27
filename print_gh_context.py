import os

print("Hello World!")

print(f"{os.environ['github.head_ref']}")
print(f"{os.environ['github.sha']}")

print("Byebye!")