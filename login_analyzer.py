

# Get analyst input

analyst = input("Enter Analyst name: ")

# user input

username = input("Enter username: ")
failed_logins = int(input("Enter number of failed login attempts: "))

critical_user = input("Is this a privileged user? (yes/no): ")

# adusting reporting

print("\n=== Login Attempt Analyzer ===")
print(f"Analyzer: {analyst}")

print("\n=== Login Attempt Summary ===")
print(f"Username: {username}")
print(f"Failed Attempts: {failed_logins}")
print(f"Privileged Account: {critical_user}")

# Critial User Logic

if failed_logins > 5 and critical_user.lower() == "yes":
    print("Risk Level: HIGH")
    print("[*] CRITICAL ALERT: Privileged account under attack!")
elif failed_logins > 5:
    print("Risk Level: MEDIUM")
    print("[!] ALERT: Multiple failed logins detected.")
elif 1 <= failed_logins <= 5:
    print("Risk Level: LOW")
    print("[!] Notic: Some Failed attempts observed.")
elif failed_logins == 0:
    print("Risk Level: Informational")
    print("[+] Info: Normal login activity observed.")

# Import and print date time

from datetime import datetime

time = datetime.now()
print("\n=== Report Generated ===")
print(time)