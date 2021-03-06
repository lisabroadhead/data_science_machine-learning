import timeit 

#  Tuple Practice:
z = (3,7,4,2)
print(z[-1])
print(z[1:2])

friends = ('Steve', 'Rachel', 'Michael', 'Monica')
for index, friend in enumerate(friends):
    print(index,friend)

animals = ("lama", "sheep","lama",28,"lama","monkey","donkey")

print(f"lama count: {animals.count('lama')}")

# Time limit
print(timeit.timeit('x=(1,2,3,4,5,6,7,8,9,10,11,12)', number=1000000))
print(timeit.timeit('x=[1,2,3,4,5,6,7,8,9,10,11,12]', number=1000000))

