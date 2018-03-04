#!/usr/bin/python
# # -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""
AutoLogin 0.1
Necessario a biblioteca selenium...
Carlos Magno
UFSJ
Referência: https://stackoverflow.com/
questions/21186327/fill-username-and-
password-using-selenium-in-python
"""
# Configuração de Login e senha.
cpf = "CPF"
minhasenha = "senha"
# Realiza o login na pagina.


def logar():
    navegador = webdriver.Firefox()
    # site base para abrir a pagina de login
    navegador.get("http://g1.com.br")
    # Id do Login
    username = navegador.find_element_by_id("ft_un")
    # Id da Senha
    senha = navegador.find_element_by_id("ft_pd")
    # usuario
    username.send_keys(cpf)
    # senha
    senha.send_keys(minhasenha)
    senha.send_keys(Keys.ENTER)
    # fecha a pagina do navegador
    navegador.close()

while(True):
	try:
		logar()
	except Exception as e:
		while(rodar):
			print "Erro na revalidação de autentificação :)."
		exit()
   
    # tempo até o proximo login
    print ("Executando.. aguardando a próxima autentificação.")
    time.sleep(1500)
