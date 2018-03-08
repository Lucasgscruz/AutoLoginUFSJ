#!/usr/bin/python
# # -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib2
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


def realizar_conexao():
	try:
		#link para verificar a conexão..
		f=urllib2.urlopen('https://www.google.com.br',timeout=1)
		#ja conectado
		#print "Já conectado"
		return False
	except Exception as e:
		#Requisitar conexão
		#print "erro",e
		return True
def logar():
	try:
		navegador = webdriver.Firefox()
		navegador.get("http://g1.com.br")
		#procura os campos correspondentes em html...
		username = navegador.find_element_by_id("ft_un")
		senha = navegador.find_element_by_id("ft_pd")
		#envia o cpf para a pagina
		username.send_keys(cpf)
		#envia a senha
		senha.send_keys(minhasenha)
		#simula o enter do navegador..
		senha.send_keys(Keys.ENTER)
	except Exception as e:
		print "Erro na conexão"
		navegador.close()
		return False

	navegador.close()
	return True

while(True):
	#verifica a permissão para realizar a conexão
	if realizar_conexao():
		print "Realizando conexao"
		if(logar()):
			print "Conectado"
		else:
			print "Erro no Login"

	else:
		print "Conexao Ok, verifição automática em 5 minutos"
		#DORME POR 5 MINUTOS
		time.sleep(300)
