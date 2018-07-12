alph=input("")
if((alph>='a'and alph<='z')or(alph>='A' and alph<='Z')):
	if alph in ['a','e','i','o','u','A','E','I','O','U']:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
