num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
med = (num1+num2)/2

if med>=7 and med<=10:
    print("Aluno aprovado.")

elif med>=4 and med<7:
    print("Aluno está apto a fazer a prova final. ")

elif med<4 and med>=0:
    print("Aluno reprovado.")

elif med>10:
    print("Algum erro com as notas inseridas. Insira novamente. ")

elif med<0:
    print("Algum erro com as notas inseridas. Insira novamente. ")