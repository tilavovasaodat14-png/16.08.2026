son = 1
while son <= 30:
  if son % 2 == 0:
    print(son)
  son += 1

  yigindi = 0
  son = int(input("Son kiriting (chiqish uchun 0 kiriting): "))

  while son != 0:
      yigindi += son
      son = int(input("Son kiriting (chiqish uchun 0 kiriting): "))

  print(f"Kiritilgan sonlar yig'indisi: {yigindi}")


parol = ""
while parol != "python123":
  parol = input("Parolni kiriting: ")
  if parol != "python123":
    print("Noto'g'ri parol! Qayta urinib ko'ring.")

print("Xush kelibsiz! Parol to'g'ri.")

N = int(input("Musbat son kiriting: "))
faktoriyal = 1
i = 1

while i <= N:
  faktoriyal *= i
  i += 1

print(f"{N} sonining faktoriali: {faktoriyal}")

N = int(input("Chegarachi sonni (N) kiriting: "))
a, b = 0, 1

print(f"{N} dan kichik Fibonachchi sonlari:")
while a < N:
  print(a, end=" ")
  a, b = b, a + b
print()

N = int(input("Son kiriting: "))

if N <= 1:
  print(f"{N} tub ham, murakkab ham emas.")
else:
  boluvchi = 2
  tub = True

  while boluvchi * boluvchi <= N:
    if N % boluvchi == 0:
      tub = False
      break
    boluvchi += 1

  if tub:
    print(f"{N} - Tub son.")
  else:
    print(f"{N} - Murakkab son.")