#Cálculo simplificado de imposto de Renda 2021
#Este programa recebe o salario digitado 
#Calcula a porcentagem de imposto Conforme a categoria que se classifica
#Calcula parcela a deduzir, e deducao por dependentes se tiver

salario= float (input("insira seu salário:R$ "))
numdependentes= int (input("Quantos dependentes possui 0 para nenhum: "))
#dependentes a deduzir
deducao=numdependentes*189.59
imposto1= (salario/100)*7.5-142.80-deducao
imposto2= (salario/100)*15-354.80-deducao
imposto3= (salario/100)*22.5-636.13-deducao
imposto4= (salario/100)*27.5-869.36-deducao


if salario < 1903.98:
    print("Isento de impostos")
elif salario < 2825.65:
    salatual= salario-imposto1
    if imposto1 < 0:
        print("Isento de impostos")
    else:
        print("Será descontado do seu salário R$",imposto1, "Salario atual R$",salatual)
elif salario < 3751.05:
    salatual= salario-imposto2
    if imposto2 < 0:
        print("Isento de impostos")
    else:
        print("Será descontado do seu salário R$",imposto2, "Salario atual R$",salatual)
elif salario < 4664.68:
    salatual= salario-imposto3
    if imposto3 < 0:
        print("Isento de impostos")
    else:
        print("Será descontado do seu salário R$",imposto3, "Salario atual R$",salatual)
    
else:
    salatual= salario-imposto4
    if imposto4 < 0:
        print("Isento de impostos")
    else:
        print("Será descontado do seu salário R$",imposto4, "Salario atual R$",salatual)
    


    
