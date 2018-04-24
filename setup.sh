#SetuP- V0.1

echo "Executando AutoSetup - Configurado para Linux"
echo "Versão Experimental 0.1"
echo "Instalando dependencias"
echo "Instalando o Pip"
sudo apt install python-pip
echo "Instalando o selenium"
sudo python -m pip install selenium
echo "Baixando O Driver do selenium"
echo "Alterando Permissão"
sudo chmod +X phantomjs
echo "Instalando Driver"
sudo mv phantomjs /usr/local/bin
echo ""
echo "Configurando dados de login"
read -p "Digite seu CPF: " cpf
printf "Digite sua senha: "
read -s senha
verifica=$( grep -ic "auto.py" ~/.bashrc) 

if [ $verifica = 0 ]
then
	echo \# configuraçao do autologin UFSJ >> ~/.bashrc
	echo alias logar=\'python /opt/autoLogin/auto.py\' >> ~/.bashrc
fi
rm config
touch config
echo $cpf >> config
echo $senha >> config

echo "Driver instalado.."
echo "Agora configure o auto.py e execute o auto.py"
echo "Obrigado, Reporte os problemas que encontrar em https://github.com/Exterminus/AutoLoginUFSJ"

sudo mkdir /opt/autoLogin
sudo cp auto.py /opt/autoLogin
sudo cp config /opt/autoLogin
 
