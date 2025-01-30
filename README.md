Requisitos
ejecuta pip install -r requirements.txt
si da error ejecuta 
Para resolver esto, puedes intentar los siguientes pasos:
Primero, actualiza la lista de paquetes:
sudo apt-get update --fix-missing
Si el problema persiste, puedes intentar cambiar a otros servidores de repositorio:
sudo sed -i 's/security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
Luego vuelve a intentar la actualización:
bashCopysudo apt-get update
sudo apt-get upgrade
