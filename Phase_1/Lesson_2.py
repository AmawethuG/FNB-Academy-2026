#The Secure Password Hint Tool

secret_password = input("Enter your secret password: ")
secret_password.strip() # Remove any leading or trailing whitespace
if secret_password: # Check if the password is not empty
    print( f"your password contains: {secret_password[0]}", end="") # Print the first character
    print("*" * (len(secret_password) - 2), end="") # Print asterisks for the middle characters
    print(  f"{secret_password[-1]}") # Print the last character