/*
Código para testar o pySerial para comunicação com o Arduino
Autor: @DjEdu28 - Luis Eduardo
Feiro em: 02/06/2024
Ultima atualização: 02/06/2024
Motivo: ajudar o amigo Daniel, gp Automação e IOT

A. Esse código espera um texto pela serial e o devolve na mesma serial,
   escrevendo 
   "ok - " antes do texto recebido
*/

void setup() {
  // initialize serial:
  Serial.begin(9600);
  Serial.println("INICIADO...");
  delay(100);
}


void loop() {
  if (Serial.available()) {
    String inputString =  Serial.readString();
    Serial.print("ok - ");
    Serial.println(inputString);
  }
}
