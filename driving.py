country = input('what country are you livng?')
age = input('how are you?')
age = int(age)
if country == "HK":
	if age >= 18:
		print('you can drive')
	else:
		print('you cannot drive')
elif country == "US":
	if age >= 16:
		print('you can drive')
	else:
		print('you cannot drive')
