def palindrome(s):
	reverse = s[::-1]
	if reverse == s:
		return f"{s} is palindrome string"
	else:
		return f"{s} is not palindrome string"

print(palindrome("madam"))