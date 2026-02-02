def sum(*args):
    #Args is tuple of all the items passed to sum
    total=0
    for item in args:
        total+=item
    return total
    
print(sum(5,5,5,5,4,5,6,5))
# def sum(*args):
#     total=0
#     for item in args:
#         total+=item
#     return total
# print(sum(10,10,10,10,10,10))

# def my_function(*args):
#     print(type(args))
#     for arg in args:
#         print(arg)
# my_function(1,2,3,4,"Hello")
# my_function()
# my_function("a","b")