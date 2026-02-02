# python-day-29
Day 24 of my python journey
Today i learn i about
(1)The walrus operator ( := ), introduced in Python 3.8, is an assignment expression operator. It allows you to assign a value to a variable within an expression. This can make your code more concise and, in some cases, more efficient by avoiding repeated calculations or function calls. The name “walrus operator” comes from the operator’s resemblance to the eyes and tusks of a walrus.
use cases of walrus operator:
1) Conditional Expressions:
2)List Comprehensions:
3)Reading Files

(2)Args
*args collects any extra positional arguments passed to a function into a tuple. The name args is just a convention; you could use any valid variable name preceded by a single asterisk (e.g., *values , *numbers )
lets understand it
suppose i create a function called "Sum". That stores inside of it *args
now i create a variable Total that stores 0 now i use for loop for item in args now inside of it i sum total+=item and return Total now i create print function and that add numbers inside of it now the output is sum of all the number come .
3)Kwargs
**kwargs collects any extra keyword arguments passed to a function into a dictionary. Again, kwargs is the conventional name, but you could use any valid variable name preceded by two asterisks (e.g., **data , **options)
lets understand it :
suppose i create a simple marks function that stores **kwargs inside of it
now i use for loop for item in kwags.keys(): now understand what happen here the keys () are convert to dictionaries inside it.
now we use print and f string to print items and values of it , in our case the values is kwargs. now i give inputs like yash=50,divesh=40,dhanes=30 that stores in our kwarg now the output comes like this 
yash:"50"
divesh:"40"
dhanesh:"30"
thats easy to i understand
(4) combination of args and kwargs
You can use both *args and **kwargs in the same function definition. The order is important: *args must come before **kwargs . You can also include regular positional and keyword parameters.
lets understand it:
suppose i create a function called func1 right? now it stores *Args and **Kwargs inside of it after that i print both of it now i give input right? Now i call function "func1" and add my values like 1,2,3,4,yash=50,yashu=60,manish=80
the output look like this 
(1, 2, 3, 4, 5) This is args 
{'yash': 50, 'yashu': 60, 'manish': 20} This is Kwargs
lets end it
