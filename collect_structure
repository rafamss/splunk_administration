#######################################
## Coleta e Encaminhamento de Dados ##
## Criado em: 18/10/2019            ##
## Criador: Rafael Martins          ##
#######################################

Encaminhar dados do UF para o HF
Para que os dados coletados pelo Universal Forwarder sejam encaminhados ao Heavy Forwarder e consequentemente indexados e apresentados na(s) Search Head(s), é necessário a criação e/ou edição de arquivos e/ou configurações conforme a ordem dos passos a saber:

--> Configuração Universal Forwarder
Sugere-se a criação de um aplicativo para cada nova coleta e inserir os arquivos de configuração inputs.conf e outputs.conf ambos com as devidas configurações, conforme:

/opt/splunkforwarder/etc/apps/local_collect/local

--> inputs.conf

[monitor:///var/log/messages]
disabled = 0
index = splk_idx
sourcetype = unixlog

[monitor:///var/log/audit]
disabled = 0
index = splk_idx
sourcetype = unixlog

--> outputs.conf

[tcpout]
defaultGroup=my_HFs

[tcpout:my_HFs]
server=IP:PORTA

--> Configuração Heavy Forwarder
Deve-se aplicar a configuração na Interface Web ou via CLI, a saber:
 
Receive data: 9997
Forwarding data: IDX_IP:PORTA

->> Configuração Indexer
Deve-se aplicar a configuração na Interface Web ou via CLI, a saber:

--> Criar o Index conforme configurado no Universal Forwarder, nesse caso: splk_idx
Receive data: 9997

--> Configuração Search Head
Deve-se aplicar a configuração na Interface Web ou via CLI, a saber:

Search Peers:
IDX_IP:PORTA
