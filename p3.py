a =121
if str(a) == str(a)[::-1]:
   print("palindrome")
else:
   print("not palindrome")



#-------------------
positive = []
negetive = []
zero = []
 
all = list(range(-25,26))
for i in all:
   if i > 0:
      positive.append(i)
   elif i < 0:
      negetive.append(i)
   else:
      zero.append(i)
print("Positive:" ,positive)
print("Negetive:",negetive)
print("Zero:",zero)
