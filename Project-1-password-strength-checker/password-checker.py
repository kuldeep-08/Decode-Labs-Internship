from pyfiglet import Figlet
from colorama import Fore,Style,init
import string

init()

banner=Figlet(font="big")
print(Fore.GREEN + banner.renderText("PASSWD") + Style.RESET_ALL)
print(Fore.YELLOW + "PASSWORD STRENGTH CHECKER\n") 

password = input("Enter Password: ")

score = 0

print("\nPASSWORD CHECK\n")

# 1. Length
if len(password) >= 8:
    print("Length: OK ✔")
    score += 1
else:
    print("Length: MISSING ❌")

# 2. Uppercase
if any(c.isupper() for c in password):
    print("Uppercase: OK ✔")
    score += 1
else:
    print("Uppercase: MISSING ❌")

# 3. Lowercase
if any(c.islower() for c in password):
    print("Lowercase: OK ✔")
    score += 1
else:
    print("Lowercase: MISSING ❌")

# 4. Number
if any(c.isdigit() for c in password):
    print("Number: OK ✔")
    score += 1
else:
    print("Number: MISSING ❌")

# 5. Special character
if any(c in string.punctuation for c in password):
    print("Special: OK ✔")
    score += 1
else:
    print("Special: MISSING ❌")

# Rating
print("\nRating:", score, "/5")

# Result
if score == 5:
    print("VERY STRONG 💪")
elif score == 4:
    print("STRONG ✅")
elif score == 3:
    print("GOOD 👍")
elif score == 2:
    print("WEAK ⚠️")
else:
    print("VERY WEAK ❌")

# Simple suggestions
if score == 5:
    print("\n✔ Your password is strong and secure!")

else:
	print("\nImprove your password:")
if len(password) < 8:
	print("- Make it at least 8 characters")
if not any(c.isupper() for c in password):
    	print("- Add uppercase letter")
if not any(c.islower() for c in password):
	print("- Add lowercase letter")
if not any(c.isdigit() for c in password):
	print("- Add number")
if not any(c in string.punctuation for c in password):
    print("- Add special character")
