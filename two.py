import one


print("Top level in two.py")
one.func()
one.new()
if __name__=='__main__':
    print("two.py is being run directly!")
else: 
    print("two has been imported...")

