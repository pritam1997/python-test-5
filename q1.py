def max(p,q,r):
	if p==q==r:
		print("All are same number")
	elif p>q:
		if p>r:
			print("1st no. is greater")
		elif r>q:
			print("3rd no. is greater")
	elif q>r:
		print("2nd no. is greater")
	else:
		print("3rd no. is greater")


a=int(input("Enter 1st no. : "))
b=int(input("Enter 2nd no. : "))
c=int(input("Enter 3rd no. : "))
max(a,b,c)