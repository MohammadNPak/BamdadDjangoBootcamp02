
def my_func(*args,**kwargs):
    print(args)
    print(kwargs)


my_func(2,3,4,5,6,7,8,a=2)



a = []
for i in range(10):
    if i%2==0:
        a.append(i)


# list comprehentions
a = [i for i in range(10) if i%2==0]