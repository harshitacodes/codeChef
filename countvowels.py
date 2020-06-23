# user_input = input("Please Enter Your Own String : ")
# vowels = 0
# consonants = 0

# for i in user_input:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
#        or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1

# print("Vowels = ", vowels)

# print("Consonants = ", consonants)





vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vow = 0
const = 0
a = input("enter the string ")
i = 0 
while i < len(a):
	w = "not vowel"
	j = 0
	while j < len(vowels):
		if a[i] == vowels[j]:
			vow = vow + 1
			w = "vowel"
			break
		j = j + 1
	if w == "not vowel":
		k = 0
		while k < len(consonants):
			if a[i] == consonants[k]:
				const = const + 1
				break
			k = k + 1	
	i = i + 1
print(vow)
print(const)




		

