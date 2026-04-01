email=input("Enter your Email:")
parts=email.split("@")
username=parts[0]
domain=parts[1]
print("Username",username)
print("Domain",domain)