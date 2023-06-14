# This allows you to call a function by its name
#
# Examples include a function with args and one without

def yo():
    return 'yo'

def hi(*args):
    return " ".join(args)

func_name1 = "yo"
func_name2 = "hi"

func1 = globals()[func_name1]
func2 = globals()[func_name2]

res1 = func1()
print(res1)

res2 = func2("Hello,","world!")
print(res2)
