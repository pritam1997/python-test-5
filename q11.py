g = "Ajay@tcs.com"

s=str()
for i in g:
	if i == '@':
		break
	s=s+i
i = g.index('@')

s2=''
for a in range(i+1,len(g)):
	if g[a]=='.':
		break
	s2 += g[a]
print(f"Username is {s} and company name is {s2}")
