text = input("soz kiriting :")
teskari_soz = text[::-1]
if text == teskari_soz:
   print(f"Palindrom so'z '{text}'")
else:
   print(f"Palindrom emas '{text}'")