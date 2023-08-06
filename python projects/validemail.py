email = input("Enter your Email : ")
j,k,l = 0,0,0

if len(email)>=6:
    if ("@" in email) and (email.count("@") == 1):
        if (email[-3] == ".") ^ (email[-4] == "."):
            for i in email:
                if i == i.isspace():
                    j = 1
                elif i.isalpha():
                    if i == i.upper():
                        k = 1
                elif i.isdigit():
                    continue
                elif i == "_" or i == "@" or i == ".":
                    continue
                else :
                    l = 1
            if j == 1 or k == 1 or l == 1:
                print("Email not contain space,upperletter and special character!!")
            else:
                print("Email validate successfully!!")
        else:
            print("Email not conatin '.' one after another!!")
    else:
        print("Email not contain more than 1 \"@\"!!")
else:
    print("Email contain atleast 6 character!!")