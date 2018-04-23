# AutoLoginUFSJ
AutoLogin para sistema de autentificação da UFSJ v.0.1

* Instalador Automático, testado para Ubuntu 16.04
* Em desenvolvimento..
* Testado para conexão ethernet, via cabo.
* Funcional.


# Requisitos
* Biblioteca Selenium..
* PhantomDriver

# Instalação Automática Para Sistemas Linux

Execute o aquivo setup.sh no terminal.

> sudo ./setup.sh


# Instalação Manual

Instalando o Selenium
 > pip install -U selenium

Instalando o Driver..

Baixe o drive em:
> https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

Descompacte o arquivo e modifique a permissão de execução do phantom dentro da pasta bin:
> chmod +x phantomjs

Agora mova o arquivo para o diretorio:
> /usr/local/bin


# Configure o seu login

Abra o auto.py e configure:

* cpf(Cpf usado para acessar a intranet.)
* minhasenha(sua senha da intranet.)

# Personalizando o comando de login

Você pode criar um alias para facilitar a execução do mesmo via terminal seguindo os seguintes passos:
* Descompacte o arquivo AutoLoginUFSJ na sua pasta home
* Edite o arquivo .bashrc que está oculto na sua home.
* No ubuntu execute:
> gedit .bashrc

* Adicione a seguinte linha no arquivo
> alias logar="python AutoLoginUFSJ/auto.py"

* Salve o arquivo.
* Abra um novo terminal e digite o comando logar.

# Como usuar

Execute no terminal :
>python auto.py

Execute antes de realizar o login..


# Como Ajudar..
* Reporte problemas e envie sugestões.
* Exerça o seu direto de fork :) !.
* Contribua adicionando issues.
