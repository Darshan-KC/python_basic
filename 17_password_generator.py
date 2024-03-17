# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random
special = ['!','@','#','$','%','&','*','+','-','_','=']

# Generate password
def password(ch):
    password = list()
    if ch =='w':
        n = random.randint(1,4)
        for x in range(0,n):
            tem = random.randint(97,122)
            password.append(chr(tem))
        return ''.join(password)
    
    elif ch == 'm':
        n = random.randint(4,8)
        for x in range(0,n):
            c = random.randint(0,1)
            if c == 1:
                tem = random.randint(65,90)
                password.append(chr(tem))
            else:
                tem = random.randint(97,122)
                password.append(chr(tem))
        return ''.join(password)
    
    elif ch == 's':
        n = random.randint(8,12)
        for x in range(0,n):
            c = random.randint(0,2)
            if c == 0:
                tem = random.randint(97,122)
                password.append(chr(tem))
            elif c == 1:
                tem = random.randint(65,90)
                password.append(chr(tem))
            else:
                tem = random.randint(0,(len(special) - 1))
                password.append(special[tem])
        return ''.join(password)
    else:
        n = random.randint(8,16)
        for x in range(0,n):
            c = random.randint(0,3)
            if c == 0:
                tem = random.randint(97,122)
                password.append(chr(tem))
            elif c == 1:
                tem = random.randint(65,90)
                password.append(chr(tem))
            elif c == 2:
                tem = random.randint(0,(len(special) - 1))
                password.append(special[tem])
            else:
                tem = random.randint(0,9)
                password.append(str(tem))
        return ''.join(password)

print("Enter w for very weak password, m for weak password, s for strong password, v for very strong password: ")
choice = input("Enter your choice : ")
if(not (choice == 'w' or choice == 'm' or choice == 's' or choice == 'v')):
    print("Invalid input")
    
else:
    print(password(choice))