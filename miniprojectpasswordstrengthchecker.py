import re

def check_password_strength(password):
    
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if re.search(r'[A-Z]', password):  
        score += 1
    if re.search(r'[a-z]', password):  
        score += 1
    if re.search(r'\d', password):     
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    weak_patterns = ['123', 'password', 'qwerty', 'abc']
    if any(pattern in password.lower() for pattern in weak_patterns):
        score -= 2
        
    if score >= 6:
        return "Strong"
    elif score >= 4:
        return "Moderate"
    else:
        return "Weak"
    
user_password = input("Enter your password: ")
strength = check_password_strength(user_password)
print(f"Password Strength: {strength}")
