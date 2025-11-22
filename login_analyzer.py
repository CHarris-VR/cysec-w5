
# user input

username = input("Enter username: ")
failed_logins = int(input("Enter number of failed login attempts: "))

if failed_logins > 5:
    print(f"[!] ALERT: {username} has {failed_logins} failed logins!")
else:
    print(f"User {username} appears normal.")

# adding critical user

critical_user = input("Is this a privileged user? (yes/no): ")

if failed_logins > 5 and critical_user.lower() == "yes":
    print("[*] CRITICAL ALERT: Privileged account under attack!")
elif failed_logins > 5:
    print("[!] ALERT: Multiple failed logins detected.")
elif failed_logins > 0:
    print("[-] Notice: Some failed attempts observed.")
else:
    print("[+] No failed logins recorded.")

# adding reporting

print("\n=== Login Attempt Summary ===")
print(f"Username: {username}")
print(f"Failed Attempts: {failed_logins}")
print(f"Privileged Account: {critical_user}")

