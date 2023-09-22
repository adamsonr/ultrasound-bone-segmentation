
#include <Arduino.h>
#define dirPin 2
#define stepPin 3
#define stepsize 1000
void setup() {
  // Declare pins as output:
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600, SERIAL_8N1);
  Serial.println("Arduino ready for action!");

  // Set the spinning direction CW/CCW:
}
void move() {
  // These four lines result in 1 step:
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(500);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(500);
}


void loop() {
  while (1) 
  {
    if (Serial.available() > 0) 
    {
      
      // read the incoming byte:
      int inByte = Serial.read();
      int dir=0;
      switch (inByte)
      {
        case (int) 'f': dir=0;a
        case (int) 'b': dir=1;
      }
      Serial.print(dir);

      switch (dir)
      {
        case 0:
          {
              for (int i=0;i<stepsize;i++)
              {
                  digitalWrite(dirPin, LOW);
                  move();
              }
              Serial.print("Moved ");
              Serial.print(stepsize);
              Serial.print("\r\n");
              break;
          }
          case 1:
          {
              for (int i=0;i<stepsize;i++)
              {
                  digitalWrite(dirPin, HIGH);
                  move();
              }
              Serial.print("Moved ");
              Serial.print(-stepsize);
              Serial.print("\r\n");
              break;
              
          }
        }
      } 
    }
  }

  
