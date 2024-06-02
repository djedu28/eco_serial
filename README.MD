# Código para testar o pySerial para comunicação com o Arduino

* Autor: @DjEdu28 - Luis Eduardo
* Feiro em: 02/06/2024
* Ultima atualização: 02/06/2024

* Motivo: ajudar o amigo Daniel, gp Automação e IOT.

Este teste é dividido em duas pates, o código no Arduino e o código python para rodar no pc

## No Arduino:

Não é necessário instalar nenhuma biblioteca externa, basta carregar o código no Arduino  [./eco_serial.ino](./eco_serial.ino) 

Esse código espera um texto pela serial e o devolve na mesma serial,
escrevendo "ok - " antes do texto recebido

## No python (PC)

É necessário ter o python 3 e a biblioteca pySerial instalada

### Para instalar a biblioteca pySerial
```bash
pip install pySerial
```

### O que esse código faz?
Esse código envia um texto para o Arduino e espera o eco de volta e o exibe em tela.

Dividido em duas etapas,
A. ele envia um texto pre programado e aguarda o retorno
B. depois inicia um loop monitor serial: 
    1 - aguardando o input do python e depois 
    2 - enviando esse input para o Arduino, depois 
    3 - exibindo o eco do Arduino
    4 - voltando ao ponto 1
	
### Para executar esse código no Arduino:

No windows, apenas de 2 cliques rápidos no arquivo `pc_python.py`

ou 

Abra o terminal na pasta e execute o comando
```bash
py ./pc_python.py
```
