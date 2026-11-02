nums=[1,2,3,4]
result=map(lambda x:x**2,nums)  #it returns map object. a map object is an iterator, which means that it generates the values on-the-fly as you iterate over it. It does not store all the values in memory at once.
print(list(result))

nums=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,nums)) # it returns a filter object. A filter object is also an iterator, which means that it generates the values on-the-fly as you iterate over it. It does not store all the values in memory at once.
print(result)

