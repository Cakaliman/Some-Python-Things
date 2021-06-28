import string
import random



print("=-=-=-=-Gerador de Senhas=-=-=-=- \n\n")

#tamanho da senha solicitada
tam = int(input("Tamanho da senha: "))

'''
EM CONSRTUÇÃO

#permite escolha de caracteres
while (True):
    opt1 = int(input("\nCom maiusculas? "))
    opt2 = int(input("Com minusculas? "))
    opt4 = int(input("Com numeros?    "))
    opt3 = int(input("Com pontuação?  "))

    #condição de existencia
    if   (opt1 == 0 or opt2== 0 or opt3== 0 or opt4 == 0): 
        x = 0 
        print("Preencha 1 campo pelo menos")
    elif (opt1 != 0 and 1 or opt2 != 0 and 1 or opt3 != 0 and 1 or opt4 != 0 and 1):
        print("1 ou 0 apenas")
    else: 
        ("ok")
        break


#inicia a logica de geração de senhas
x[3]= (opt1, opt2, opt3, opt4)
'''

low = string.ascii_lowercase
upp = string.ascii_uppercase
num = string.digits
sym = string.punctuation


all = low + upp + num + sym

temp = random.sample(all, tam)

print(temp)


'''
def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]

'''
