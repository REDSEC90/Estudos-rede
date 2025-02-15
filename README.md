Ola este repositorio é para fins educacionais!

a intencao deste repositorio é criar um script altamente explicativo para criacao
de um ponto de acesso(WIFI-FALSO) Para fins de estudo de ciberseguranca.

para comecar os estudos deve-se configurar primeiramente um wifi.
usando "dnsmasq" para fornecer ip, e "hostapd" para emular um ponto de acesso.

##para configura-los usa-se os comandos abaixo

sudo apt updatw

sudo apt install hostapd dnsmasq

##o comando acima talvez nao seja necessario caso ja esteja instalado 

sudo ip link set wlan0 down

sudo iw dev wlan0 set type monitor

sudo ip link set wlan0 up

##ative o ponto de acesso com o comando abaixo

sudo hostapd hostapd.conf

##ative o dnsmask

sudo dnsmasq -C dnsmasq.conf

## VERIFIQUE SE A REDE FOI CRIADA E SE É POSSIVEL IDENTIFICALA PELO NOME(SSID)

##NOME DE REDE: FakeWiFiNetwork

## APOS ISSO PODEMOS INICIAR COM A TENTATIVA DE CAPTURAR A SENHA DO WIFI.

## temos "aircrack-ng" captura pacotes e tenta quebrar a senha

## e temos ataque de forca bruta com "reaver" entre outros.

