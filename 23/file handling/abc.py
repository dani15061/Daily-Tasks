import string
def letters(n):
   with open("words1.txt", "w") as f:
       alph = string.ascii_uppercase
       letter = [alph[i:i + n] + "\n" for i in range(0, len(alph), n)]
       f.writelines(letter)
letters(3)