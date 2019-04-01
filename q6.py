s1 = input("Enter 1st string : ")
s2 = input("Enter 2nd string : ")

def maxlength():
	if len(s1) == len(s2):
		return f"Both string having same length \n{s1}\n{s2}"
	elif len(s1) > len(s2):
		return f"1st string having length : {len(s1)}\n{s1}"
	else:
		return f"2nd string having length : {len(s2)}\n{s2}"

print(maxlength())