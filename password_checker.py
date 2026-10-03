def check_password_strength(password):
    length = len(password)

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    # Common password check
    common_passwords = [
        "password",
        "12345678",
        "123456789",
        "qwerty",
        "password123",
        "admin",
        "welcome"
    ]

    is_common = password.lower() in common_passwords

    # Calculate score
    score = 0

    if length >= 8:
        score += 1

    if length >= 12:
        score += 1

    if length >= 16:
        score += 1

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    # Determine strength
    if is_common:
        strength = "Weak"
    elif score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Calculate percentage
    percentage = round((score / 7) * 100)

    print("\nPassword Strength:", strength)
    print("Security Score:", score, "/ 7")
    print("Security Level:", percentage, "%")

    # Common password warning
    if is_common:
        print("\n⚠ Warning: This is a commonly used password.")

    # Password analysis
    print("\nPassword Analysis:")

    if length >= 8:
        print("✓ Length is at least 8 characters")
    else:
        print("✗ Password should be at least 8 characters")

    if length >= 12:
        print("✓ Length is at least 12 characters")
    else:
        print("✗ Consider using at least 12 characters")

    if length >= 16:
        print("✓ Length is at least 16 characters")
    else:
        print("✗ Consider using 16 or more characters")

    if has_uppercase:
        print("✓ Contains uppercase letter")
    else:
        print("✗ No uppercase letter")

    if has_lowercase:
        print("✓ Contains lowercase letter")
    else:
        print("✗ No lowercase letter")

    if has_digit:
        print("✓ Contains number")
    else:
        print("✗ No number")

    if has_special:
        print("✓ Contains special character")
    else:
        print("✗ No special character")

    # Suggestions
    print("\nSuggestions:")

    suggestions = False

    if length < 8:
        print("- Use at least 8 characters")
        suggestions = True

    if length < 12:
        print("- Consider using at least 12 characters")
        suggestions = True

    if not has_uppercase:
        print("- Add an uppercase letter")
        suggestions = True

    if not has_lowercase:
        print("- Add a lowercase letter")
        suggestions = True

    if not has_digit:
        print("- Add a number")
        suggestions = True

    if not has_special:
        print("- Add a special character")
        suggestions = True

    if is_common:
        print("- Avoid commonly used passwords")
        suggestions = True

    if not suggestions:
        print("✓ No basic improvements needed")


# Main menu
while True:
    print("\n==============================")
    print("   PASSWORD STRENGTH CHECKER")
    print("==============================")
    print("1. Check Password")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        password = input("\nEnter a password: ")
        check_password_strength(password)

    elif choice == "2":
        print("\nThank you for using Password Strength Checker!")
        break

    else:
        print("\nInvalid choice. Please enter 1 or 2.")