
username = input("Enter username: ")
failed_logins = int(input("Enter number of failed login attempts: "))

if failed_logins > 5:
    print(f"[!] ALERT: {username} has {failed_logins} failed logins!")
else:
    print(f"User {username} appears normal.")