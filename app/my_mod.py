#this the app/my_mod.py

#here is a normal version:
"""
def enlarge(n):
return n *100
"""

def enlarge(n):
    """ this is a docstring
    This function enlarges a number
    pass in n as a string 
    returns a larger number
    """
    return float(n) *100

if __name__ == "__main__":


    x = input("Please input a number: ")
    result = enlarge(x)
    print(result)