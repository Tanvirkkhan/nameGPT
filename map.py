# Description: This is a simple script to test the functionality of the map function in python
# syntax: map(function, iterable, ...)
# Define a function to be used in the map function
def square(x):
    return x * x


# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map function to square each number in the list
result = map(square, numbers)

# Print the result
print(list(result))

# example with 2 lists


def add(x, y):
    return x + y


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

result = map(add, numbers1, numbers2)
print(list(result))

# example with lambda function
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x / 100, numbers)
print(list(result), type(list(result)))

# type for each element in the list
print(type(list(result)[0]))

# example with 2 lists
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
result = map(lambda x, y: x + y, numbers1, numbers2)

# write the original map function in python


def my_map(func, *iterables):
    # get the number of iterables
    n = len(iterables)
    # get the number of elements in the first iterable
    m = len(iterables[0])
    # iterate over the elements in the first iterable
    for i in range(m):
        # get the i-th element from each iterable
        args = [iterables[j][i] for j in range(n)]
        # call the function with the arguments
        yield func(*args)
