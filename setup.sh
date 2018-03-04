#SetuP- V0.1

echo "Executando AutoSetup - Configurado para Ubuntu"
echo "Versão Experimental 0.1"
echo "Instalando dependencias"
echo "Instalando o Pip"
sudo apt install python-pip
echo "Instalando o selenium"
sudo python -m pip install selenium
echo "Baixando O Driver do selenium"
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
tar -vzxf geckodriver-v0.19.1-linux64.tar.gz
echo "Alterando Permissão"
sudo chmod +X geckodriver
echo "Instalando Driver"
sudo mv /usr/local/bin geckodriver
echo "Driver instalado.."
echo "Agora configure o auto.py e execute o auto.py"
echo "Obrigado, Reporte os problemas que encontrar em https://github.com/Exterminus/AutoLoginUFSJ"
