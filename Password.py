TWHITE = '\033[37m'
TGREEN = '\033[32m'
TRED = '\033[31m'
TBLUE = '\033[34m'
password = input("Set your password : ")
a = "a" in password or "A" in password
b = "b" in password or "B" in password
c = "c" in password or "C" in password
d = "d" in password or "D" in password
e = "e" in password or "E" in password
f = "f" in password or "F" in password
g = "g" in password or "G" in password
h = "h" in password or "H" in password
i = "i" in password or "I" in password
j = "j" in password or "J" in password
k = "k" in password or "K" in password
l = "l" in password or "L" in password
m = "m" in password or "M" in password
n = "n" in password or "N" in password
o = "o" in password or "O" in password
p = "p" in password or "P" in password
q = "q" in password or "Q" in password
r = "r" in password or "R" in password
s = "s" in password or "S" in password
t = "t" in password or "T" in password
u = "u" in password or "U" in password
v = "v" in password or "V" in password
w = "w" in password or "W" in password
x = "x" in password or "X" in password
y = "y" in password or "Y" in password
z = "z" in password or "Z" in password
one = "1" in password
two = "2" in password
three = "3" in password
four = "4" in password
five = "5" in password
six = "6" in password
seven = "7" in password
eight = "8" in password
nine = "9" in password
zero = "0" in password
mark1 = "!" in password
mark2 = "@" in password
mark3 = "#" in password
mark4 = "$" in password
mark5 = "%" in password
mark6 = "^" in password
mark7 = "&" in password
mark8 = "*" in password
mark9 = "(" in password
mark10 = ")" in password
mark11 = "-" in password
mark12 = "_" in password
mark13 = "=" in password
mark14 = "+" in password
mark15 = "{" in password
mark16 = "}" in password
mark17 = "[" in password
mark18 = "]" in password
mark19 = "|" in password
mark20 = ":" in password
mark21 = ";" in password
mark22 = "''" in password
mark23 = "<" in password
mark24 = ">" in password
mark25 = "," in password
mark26 = "." in password
mark27 = "?" in password
mark28 = "/" in password
mark29 = "~" in password
mark30 = "`" in password
charlist = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y,z]
intlist = [one, two, three, four, five, six, seven, eight, nine, zero]
symlist = [mark1, mark2, mark3, mark4, mark5, mark6, mark7, mark8, mark9, mark10, mark11, mark12, mark13, mark14, mark15, mark16, mark17, mark18, mark19, mark20, mark21, mark22, mark23, mark24, mark25, mark26, mark27, mark28, mark29, mark30]
if len(password) >= 6:
    if (charlist.count(True) >= 1 and intlist.count(True) >= 1
            and symlist.count(True) >= 1):
        userinput = input("Enter the password : ")
        if userinput == password:
            print(TGREEN + "Access Granted", TWHITE)
            try :
                with open("Program") as file:
                    filedata = file.readlines()
                    for l in filedata:
                        print(l)
            except :
                print("Unable to Open File")
        else:
            print(TRED + "Access Denied.Try again")
    if (charlist.count(True) < 1 or intlist.count(True) < 1
            or symlist.count(True) < 1):
        print("Choose a stronger password")
else:
    print("Password must contain six digits")
