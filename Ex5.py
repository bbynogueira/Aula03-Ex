# Infantil A: 5 a 7 anos;
#  Infantil B: 8 a 10 anos;
#  Juvenil A: 11 a 13 anos;
#  Juvenil B: 14 a 17 anos;
#  Sênior: maiores de 18 anos

idade = int(input())

if idade>=5 and idade <=7:
    print("Infantil A")
elif idade>=8 and idade<=10:
    print("Infantil B")
elif idade>=11 and idade<=13:
    print("Juvenil A")
elif idade>=14 and idade<=17:
    print("Juvenil B")
elif idade>=18:
    print("Sênior")
