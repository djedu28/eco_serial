"""
Codigo para testar o pySerial para comunicação com o arduino
Autor: @DjEdu28 - Luis Eduardo
Feiro em: 02/06/2024
Ultima atualização: 02/06/2024
Motivo: ajudar o amigo Daniel, gp Automação e IOT

A. Esse codigo envia um texto para o arduino e espera o eco de volta e o exibe em tela.
B. depois inicia um loop monitor serial: 
    1 - aguardando o input do python e depois 
    2 - enviando esse input para o arduino, depois 
    3 - exibindo o eco do arduino
    4 - voltando ao ponto 1
"""
print("# Codigo para testar o pySerial para comunicação com o arduino\n\n")

from time import sleep # para aguardar um tempo, similar ao delay do arduino
from serial import Serial # importando Serial de dentro da biblioteca serial

# DEFININDO A PORTA USB ONDE O ARDUINO ESTÁ CONECTADO
# portaUSB  linux   '/dev/ttyUSB0'
# portaUSB  windows 'COM3'
portaUSB = 'COM8'

# UM DOS MODOS DE INSTANCIAR O SERIAL É ATRIBUINDO A UMA VARAIVEL, MAS PRECISA LEMBRAR DE FECHALO ANTES DE TERMINAR O CODIGO
#arduino=Serial(portaUSB, 9600);

# TESTANDO SE SERIAL É ACESSIVEL
try:
    arduino = Serial(portaUSB, 9600);
    arduino.close()
except:
    print(f"""
    \n=================================
    ERRO    
    
    Serial na porta '{portaUSB}' não é acessivel pelo python, 
    - verifique a variavel `portaUSB`, ela deve ser o endereço do arduino, 
      no padrão 'COMX' no windows ou '/dev/ttyUSBX' no linux
    - se o problema persistir feche o arduino IDE e tudo que possa estar acessando essa porta serial
    \n=================================""")
    input();
    exit(1);
    
# UTILIZANDO O LAÇO WITH, NÃO PRECISAMOS NOS PREOCUPAR COM O FECHAMENTO DA PORTA (PYTHON 3)
with Serial(portaUSB, 9600) as arduino:
    sleep(4)
    while arduino.in_waiting > 0:
        resposta = arduino.read_all();
        print("<= arduino:",resposta);
    
    # ENVIANDO TEXTO PARA O ARDUINO
    enviar = b"testando\n"; # o b antes da " indica que é binario
    print("=> python: ", enviar);
    arduino.write(enviar);
    sleep(1);
    # ARGUARDANDO RESPOSTA DO ARDUINO
    while (arduino.in_waiting == 0):
        print(".",flush=True,end="")
        sleep(.300)
    print(); #pulando linha para separar dos pontos
    # RECEBENDO RESPOSTA DO ARDUINO
    resposta = arduino.read_all();
    print("<= arduino:", resposta); #repara no print que a resposta é em binario
    
    print("\n","-"*40) # EXIBINDO UMA LINHA
    # ATIVANDO MODO SERIAL
    print(
        "Ativando loop monitor serial",
        "Use ctrl+C para sair do loop",
        sep="\n"
    );
    while(True): # LOOP INFINITO PARA ENVIAR TEXTO E ESPERAR ECO DO ARDUINO
        # LENDO DADOS E CONVERTENDO EM BINARIO
        enviar = input("=> python: ").encode('utf-8')
        # ENVIADNDO O INPUT PARA O ARDUINO
        arduino.write(enviar);
        # ARGUARDANDO RESPOSTA DO ARDUINO
        while (arduino.in_waiting == 0):
            print(".",flush=True,end="")
            sleep(.300)
        print(); #PULANDO LINHA PARA SEPARAR DOS PONTOS
        # EXIBINDO RESPOSTA do arduino
        while arduino.in_waiting > 0:
            sleep(.500)
            resposta = arduino.read_all();
            resposta = resposta.decode('utf-8') # Converte o array de bytes recebido para String
            print("<= arduino:",resposta,end="");

# UTILIZANDO O LAÇO WITH, NÃO PRECISAMOS NOS PREOCUPAR COM O FECHAMENTO DA PORTA (PYTHON 3)
# arduino.close()

# UM INPUT PARA SEGURAR O TERMINAL ABERTO ANTES DE FECHAR, CASO ABERTO DIRETAMENTE
input();