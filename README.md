# Data-Oriented Programming
This repository is a simple code-along based in [this article](https://towardsdatascience.com/data-oriented-programming-with-python-ef478c43a874).

The article illustrates some concepts of the book [Data-Oriented Programming by Yehonathan Sharvit](https://www.manning.com/books/data-oriented-programming) with python code.

## My main takeaways

### Separating data from the code that operates it.
I found this practice very interesting, especially for data engineering projects.

Dataclasses can be very useful for this purpose.

However, [Pydantic](https://docs.pydantic.dev/latest/) offers the same functionality with a lot of additional validation options.

### Data should be immutable
This practice is extremely important to guarantee the integrity of data, and getting to know some tools that help with it was very interesting.

Dataclasses offer the `frozen` attribute, and Pydantic has [allow_mutation](https://docs.pydantic.dev/latest/usage/model_config/) and a beta version of `frozen` (at the time of writing).

To verify if an object is immutable or not in Python, we can use the `id()` function and the `==` and `is` operators.
