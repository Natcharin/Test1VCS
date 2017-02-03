import random

def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    b = sum(alist)
    assert (x > 0 ),"cannnot be null"
    return alist
    
    """
    print a generated list
    """
def printIT():
    print(generate_list())
    
def main():
    printIT()
    print(b)
    
    """
    If this script file is called, it will run main() directly
    """
if __name__ == '__main__':
    print("Test printIT():")
    main()