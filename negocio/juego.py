import random
import pickle

def jugar(a, b):
   if a == b:
    return "Ok"
   else: return 'incorrecto'

def eligir_numero_secreto():
   numero_secreto = random.randint(0,9)
   pickle.dump(numero_secreto, open("secret_number.txt", "wb")) 

def intentar_adivinar(conjectura):
   numero_secreto = pickle.load(open("secret_number.txt", "rb"))
   return jugar(numero_secreto, conjectura)