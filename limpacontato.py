#!/usr/bin/env python3
import requests
import phonenumbers
import json
import mimetypes
import time
import os

## TODO: colocar um intervalo entre as mensagens e também entre o envio pra cada contato.
# variaveis
lista = "./lista.txt"
novalista = []

def arquivar(nomedoarquivo,texto):
	name = nomedoarquivo +'.txt'

	try:
		file = open(name,'w+')
		file.writelines(texto)
		file.close()

	except:
		print('Deu merda berg... Corre vai explodir! -qq')
		time.sleep(3)
		sys.exit(0)

def enviarParaLista():
    # realiza o envio das mensagens para a lista
    with open(lista) as file:
        for line in file:
            line = line.strip()
            try:
                line_number = phonenumbers.parse(line, "BR")
                if phonenumbers.is_possible_number(line_number) != False:
                    print("============ Novo Número ============")
                    line = phonenumbers.format_number(line_number, phonenumbers.PhoneNumberFormat.E164)
                    print("Contato: " + line)
                    novalista.append(str(line) + '\n')
                    print("============ Fim Novo Número ============")
                else:
                    print("Não é um número válido: " + str(line))
            except phonenumbers.phonenumberutil.NumberParseException:
                print("Não é um número: " + str(line))

def main():
	# nada ainda
    enviarParaLista()
    arquivar("contatoslimpos", novalista)

main()