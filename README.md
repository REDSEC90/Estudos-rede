###Ola este repositorio é para fins educacionais!

###a intencao deste repositorio é criar um script altamente explicativo para criacao

###de um ponto de acesso(WIFI-FALSO) Para fins de estudo de ciberseguranca.

###para comecar os estudos deve-se configurar primeiramente um wifi.

###usando "dnsmasq" para fornecer ip, e "hostapd" para emular um ponto de acesso.

##para configura-los usa-se os comandos abaixo

sudo apt updatw

sudo apt install hostapd dnsmasq

##o comando acima talvez nao seja necessario caso ja esteja instalado 

## os comandos abaixo sao necessarios para...

##para colocad a interface que iremos usar em modo monitor.

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

### abaixo iremos comecar com aircrack-ng

sudo airodump-ng wlan0
#o comando acima faz analise de redes proximas. ache "FakeWiFiNetwork".

## no comando abaixo voce troca "<BSSID>" pelo mac que ira sair do comando de cima.

sudo airodump-ng --bssid <BSSID> -c 6 -w capture wlan0

##o comando acima é a parte mais importante.

##ele capura handshakes e espera uma conexao de 4 vias.

# use um celular e se conecte ao wifi com a senha que vc ja tem. assim o seu computador ira capturar
##é desta maneira que funciona a captura de handshakes.
##nao se deve fazer o mesmo em wifis reais sem autorizacao


##abaixo iremos agora fazer o mesmo mas usando WORDLIST.
##primeiro precisamos criar uma wordlist, usando um script de permutacoes.
##usaremos "reaver" para fazer o bruteforce
##antes de usar o reaver. á interface que sera usada deve estar em modo monitor.
##tambem precisamos saber do mac,interface, e canal que a rede tem.

#apos termos tudo isso iremos executar os seguintes comando abaixo 

sudo reaver -i wlan0 -b <BSSID> -c <canal> -P wordlist.txt -vv

##prontinho parabens. agora é só aguardar que o reaver ira mostrar o resultado obtido.
<CONSIDERACOES EXTREMAMENTE IMPORTANTES.>
Nao use essas ferramentas em redes reais sem autorizacao. 
qualquer uso ilegal das ferranentas
tem suas conseguencias.
É fundamental sempre obter autorização explícita 
para realizar qualquer tipo de teste de segurança em redes. 
O hacking ético deve ser conduzido de forma responsável, 
respeitando os limites legais e as regras de privacidade. 
A prática de cybersecurity é voltada para educação e proteção, e não para danos a terceiros.
