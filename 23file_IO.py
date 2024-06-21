# File IO

# # Read a file
# file = open('23.txt')
# f=file.read()
# print(f)
# file.close()

# # Write a file
# file = open("23.txt",'w')
# f = file.write("Hello, world!!")
# file.close()

# # Append a file
# file = open("23.txt",'a')
# f = file.write("\nGood morning!")
# file.close()

# # with....open(automatically close the file)
# with  open("231.txt") as f:
#     f.write("\nStart a new journy!!")


# ------------------------------------------------------------------------
# seek(), tell() and other functions
with open("23.txt",'r') as f:
    f.seek(7)  # move to the 5 byte(character) in file
    print(f.tell()) #check current position
    data = f.read(5)
    print(data)

# ---------------------------------------------------------------------------
# length of each line

with open('23.txt') as f:
    line_number = 1
    for line in f.readlines():
        print(f"length of line {line_number}: {len(line)}")
        line_number +=1
