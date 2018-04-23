#SetuP- V0.1

echo "Executando AutoSetup - Configurado para Ubuntu"
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
sudo mv geckodriver /usr/local/bin 
echo "Driver instalado.."
echo "Agora configure o auto.py e execute o auto.py"
echo "Obrigado, Reporte os problemas que encontrar em https://github.com/Exterminus/AutoLoginUFSJ"
