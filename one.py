#one.py
def func():
    print("FUNC()IN ONE.PY")
print("TOP LEVEL IN ONE.PY")
def new():
    print("Something new")
if __name__ == "__main__":
    print("One.py is being run directly!")
else:
    print("ONE.PY has been imported!")