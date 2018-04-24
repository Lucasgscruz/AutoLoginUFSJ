echo Desinstalando AutoLogin UFSJ...
sudo rm -rf /opt/autoLogin
sed -i '/UFSJ/d' ~/.bashrc
sed -i '/autoLogin/d' ~/.bashrc

