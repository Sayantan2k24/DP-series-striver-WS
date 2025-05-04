def f(index):
    if index <= 1: 
        return 1
    
    return f( index-1 ) + f(index - 2)

n = int(input("Enter the stair number: "))
print(f(n))