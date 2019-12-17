# Варіант 1
# Завдання 2
# Тодер Іван Васильович

x=float(input(" x= "))
a=float(input(" a= "))
n=int((input(" n= ")))
S = (x + a) ** 2
for i in range(n):
    S= (S + a) **2
S += a
print(S)



