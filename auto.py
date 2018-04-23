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

cpf = ""
minhasenha = ""

def verifica_senha(senha):
	"""Verifica a senha digitada"""
	if(len(senha)<1):
		print "Erro, Favor preencher o campo de login e senha."
		exit()

def realizar_conexao():
	try:
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
		navegador = webdriver.PhantomJS()
		navegador.get("http://g1.com.br")
		username = navegador.find_element_by_id("ft_un")
		senha = navegador.find_element_by_id("ft_pd")
		username.send_keys(cpf)
		senha.send_keys(minhasenha)
		senha.send_keys(Keys.ENTER)
	except Exception as e:
		print "Fechando o navegador.",e
		navegador.close()
		return False

	navegador.close()
	return True

verifica_senha(minhasenha)
while(True):
	#verifica a permissão para realizar a conexão
	if realizar_conexao():
		print "Realizando conexao"
		if(logar()):
			print "Conectado"
		else:
			print "Verificando conexão."

	else:
		print "Conexao Ok, verifição automática em 5 minutos"
		#DORME POR 5 MINUTOS
		time.sleep(300)

