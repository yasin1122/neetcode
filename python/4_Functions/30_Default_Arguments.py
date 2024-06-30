# Default values must be at the end
def greet(name, punctuation="!") -> None:
    print("Hello, " + name + punctuation)

greet("World", "!")
greet("World")