from functools import reduce
#sum of numbers
nums=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,nums)
print("Sum of numbers:", result)

#functools is a module in Python that provides higher-order functions for functional programming. It includes functions like reduce, partial, lru_cache, and wraps, which can be used to manipulate and transform functions and data structures.
# it is required to import functools module to use reduce function. The reduce function takes a binary function and a sequence of elements, and applies the function cumulatively to the elements of the sequence, reducing it to a single value. In this case, we are using reduce to calculate the sum of numbers in the nums list by applying the lambda function that adds two numbers together.
# it is not require to import functools module to use map and filter functions. The map function takes a function and a sequence of elements, and applies the function to each element of the sequence, returning a new sequence with the results. In this case, we are using map to calculate the square of each number in the nums list by applying the lambda function that squares a number. The filter function takes a function and a sequence of elements, and returns a new sequence containing only the elements for which the function returns True. In this case, we are using filter to select only the even numbers from the nums list by applying the lambda function that checks if a number is even.