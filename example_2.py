# Example illustrating identity and immutability

# String is ummutable
x = "abc"

# Note that the identity of `x` and `abc` is the same
print(f"ID of x: {id(x)}")
print(f"ID of `abc`: {id('abc')}")
print(f"x == abc: {x=='abc'}")
print(f"x is abc: {x is 'abc'}")

# List is mutable
y = [1, 2, 3]

# Note that the identity of `y` and `[1, 2, 3]` is different
print(f"ID of y: {id(y)}")
print(f"ID of `[1, 2, 3]`: {id([1, 2, 3])}")
print(f"y == [1, 2, 3]: {y==[1, 2, 3]}")
print(f"y is [1, 2, 3]: {y is [1, 2, 3]}")
