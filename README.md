
Este repositório tem fins educacionais e tem como objetivo demonstrar, de forma detalhada, a criação de um script para configurar um ponto de acesso (WiFi falso) para estudos em cibersegurança. A ideia é utilizar as ferramentas dnsmasq (para fornecer IPs) e hostapd (para emular o ponto de acesso).


---

Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes pacotes instalados:

hostapd

dnsmasq


Caso eles não estejam instalados, utilize os comandos abaixo:

# Atualiza a lista de pacotes disponíveis
sudo apt update

# Instala o hostapd e o dnsmasq (caso ainda não estejam instalados)
sudo apt install hostapd dnsmasq


---

Configurando a Interface de Rede

Para a captura de pacotes e testes, é necessário colocar a interface de rede (neste exemplo, wlan0) no modo monitor. Siga os comandos abaixo:

# Desativa a interface wlan0
sudo ip link set wlan0 down

# Configura a interface wlan0 para o modo monitor
sudo iw dev wlan0 set type monitor

# Reativa a interface wlan0
sudo ip link set wlan0 up


---

Ativando o Ponto de Acesso

1. Iniciando o hostapd:
Utilize o arquivo de configuração hostapd.conf para definir os parâmetros do ponto de acesso.

# Inicia o hostapd utilizando as configurações definidas em hostapd.conf
sudo hostapd hostapd.conf


2. Iniciando o dnsmasq:
Este serviço atribui endereços IP aos dispositivos conectados, conforme definido em dnsmasq.conf.

# Inicia o dnsmasq com o arquivo de configuração especificado
sudo dnsmasq -C dnsmasq.conf


3. Verificação:
Confirme que a rede foi criada corretamente e que o SSID está visível.
Nome da rede (SSID): FakeWiFiNetwork




---

Captura de Handshakes com Aircrack-ng

Para tentar capturar a senha do WiFi, iniciaremos a captura de handshakes usando o aircrack-ng. Siga os passos:

1. Análise das redes próximas:
Execute o comando abaixo para listar as redes disponíveis e identificar a FakeWiFiNetwork.

# Lista as redes próximas. Identifique a rede FakeWiFiNetwork e anote seu BSSID.
sudo airodump-ng wlan0


2. Captura dos handshakes:
Após identificar o BSSID (endereço MAC) da rede, inicie a captura dos handshakes. Certifique-se de informar o canal correto (no exemplo, canal 6).

# Substitua <BSSID> pelo endereço MAC da rede FakeWiFiNetwork.
# O comando captura os handshakes salvando-os no arquivo "capture".
sudo airodump-ng --bssid <BSSID> -c 6 -w capture wlan0

Dica: Conecte um dispositivo (como um celular) à rede com a senha conhecida para que a captura do handshake ocorra.



> Atenção: Utilize esses procedimentos apenas em ambientes de teste ou redes para as quais você possua autorização.




---

Ataque de Força Bruta com Reaver Usando uma Wordlist

Para aprofundar os testes, você pode utilizar uma wordlist para realizar um ataque de força bruta com a ferramenta reaver.

1. Preparação:

Crie uma wordlist utilizando um script de permutações ou outra metodologia de sua preferência.

Certifique-se de que a interface wlan0 esteja em modo monitor.

Tenha em mãos os seguintes dados: BSSID, interface e canal da rede.



2. Execução do Reaver:

# Substitua <BSSID> pelo endereço MAC da rede e <canal> pelo canal correto.
# -i especifica a interface, -b o BSSID, -c o canal, -P indica o arquivo da wordlist,
# e -vv ativa a saída detalhada para monitoramento do progresso.
sudo reaver -i wlan0 -b <BSSID> -c <canal> -P wordlist.txt -vv



Após iniciar o reaver, aguarde enquanto a ferramenta tenta descobrir a senha e exibe o resultado.


---

Considerações Importantes

Ética e Legalidade:
Nunca utilize estas ferramentas em redes reais sem autorização explícita. Qualquer uso ilegal pode ter consequências sérias.

Responsabilidade:
O hacking ético deve ser conduzido de forma responsável, sempre respeitando os limites legais e as regras de privacidade. As técnicas apresentadas são para fins educacionais e para promover a segurança da informação.



---

Este repositório foi desenvolvido para fins educacionais, incentivando a compreensão dos mecanismos envolvidos na segurança de redes WiFi. A prática de cibersegurança deve sempre visar a educação e a proteção, e nunca a violação de direitos ou a invasão de privacidade.


---

Espero que este guia detalhado seja útil para seus estudos e experimentos em ambientes controlados e autorizados.


