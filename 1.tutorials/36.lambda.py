# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))


# a =[[1, 14], [5, 6], [8,23]]
# a.sort(key=lambda x:x[1])
# print(a)


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

