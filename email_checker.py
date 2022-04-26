email = input("Enter Your Email : ")

con_1 = len(email) >=6 
con_2 = email[0].isalpha()
con_3 = "@" in email and email.count("@") == 1
con_4 = (email[-3]==".")^(email[-4] == ".")
con_5 = True
for i in email:
    if i.isalpha():
        if i == i.upper():
            con_5 = False
    elif i.isspace():
        con_5 = False
    elif i.isdecimal():
        continue
    elif i == "." or i == "@" or i =="_":
        continue
    else:
        con_5 = False

if con_1 and con_2 and con_3 and con_4 and con_5:
    print("wright Email")
else:
    print("Wrong Email")
