import re

def check_strength(password):
    score = 0
    feedback = []
    
    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Use ≥8 chars")
    
    # 2. Character variety
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))  
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))
    
    if has_upper:
        score += 1
    else:
        feedback.append("• Add uppercase (A-Z)")
        
    if has_lower:
        score += 1
    else:
        feedback.append("• Add lowercase (a-z)")
        
    if has_digit:
        score += 1
    else:
        feedback.append("• Add numbers (0-9)")
        
    if has_special:
        score += 1
    else:
        feedback.append("• Add special chars")
    
    # 4. Common patterns
    common_patterns = [r'123', r'abc', r'qwe', r'password']
    if any(re.search(pattern, password.lower()) for pattern in common_patterns):
        score -= 1
        feedback.append("• Avoid patterns like 123, abc")
    
    # Rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong "
    
    return f"\nPassword Strength: {strength} (Score: {max(0, score)}/5)\n" + "\n".join(feedback[:3])


password = input("Enter password: ")
print(check_strength(password))
