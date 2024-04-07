import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*"
length_pass = int(input("Enter the password length:"))

a = "".join(random.sample(password,length_pass))
print(f"The Password is {a}")