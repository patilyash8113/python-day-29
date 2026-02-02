def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(1,2,3,4,5,yash=50,yashu=60,manish=20)


# # def combination(*args,**kwargs):
# #     print(args)
# #     print(kwargs)

# # combination(1,2,3,4,5,6,yash=50,babul=40,manish=90,raj=70)


# def my_function(a,b,*args,c=40,**kwargs):
#     print(f"a:{a}")
#     print(f"b:{b}")
#     print(f"args:{args}")
#     print(f"c:{c}")
#     print(f"kwargs:{kwargs}")

# my_function(1,2,3,4,5,c=10,name="yash",country="India")
# # my_function(1,2)

# class animal:
#     def __init__(self,name):
#         self.name=name

# class dog(animal):
#     def __init__(self, name,breed,*args,**kwargs):
#         super().__init__(name)
#         self.breed=breed
#         print(f"arg:{args}")
#         print(f"kwargs:{kwargs}")
# dog1=dog("Yash","golden retriever")
# dog2=dog("lucy","labrador",1,2,3,colour="black",age=5)