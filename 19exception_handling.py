# Exception Handling

num = input("Enter a number:")

try:
    print(f"multiplication table of {num} is :")
    for i  in range(1, 11):
        print(f"{int(num)} X {i} = {int(num)*i}")
except:
    print("Invalid Input!!")

# Finally keyword

def main():
    try:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        c = a/b
        return c
    except:
        print("Invalid Input!!")
        return 0
    finally:  # it is mainly usefull for function
        print("sum:" ,a+b)
    # print("sum:" ,a+b)  #comment the finally block and uncomment this line and check what will happen(this line unreachable becuse of return but you need sum of a & b then use finally block)
    
r = main()
print("division:",r)
