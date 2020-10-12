char c='s';

void setup()  
{
  Serial.begin(9600);
  Serial2.begin(9600);
  Serial2.println("bLuEtOoTh InItIaTeD....");
  
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  
  digitalWrite(8,HIGH);
  digitalWrite(9,HIGH);
  digitalWrite(10,HIGH);
  digitalWrite(11,HIGH);
  Serial1.println("Stop");
}

void loop()
{
    if(Serial2.available())
    {
       c=Serial2.read();
    }
   delay(80);
  
     if(c=='s')
   {
     digitalWrite(8,HIGH);
     digitalWrite(9,HIGH);
     digitalWrite(10,HIGH);
     digitalWrite(11,HIGH);
     Serial2.println("Stop");
   }
   else if(c=='a')
   {
     digitalWrite(8,LOW);
     digitalWrite(9,HIGH);
     digitalWrite(10,LOW);
     digitalWrite(11,HIGH);
     Serial2.println("Forward");
   }
   else if(c=='b')
   {
     digitalWrite(8,HIGH);
     digitalWrite(9,LOW);
     digitalWrite(10,HIGH);
     digitalWrite(11,LOW);
     Serial2.println("Reverse");
   }
   else if(c=='c')
   {
     digitalWrite(8,LOW);
     digitalWrite(9,HIGH);
     digitalWrite(10,HIGH);
     digitalWrite(11,LOW);
     Serial2.println("Right");
   }
   else if(c=='d')
   {
     digitalWrite(8,HIGH);
     digitalWrite(9,LOW);
     digitalWrite(10,LOW);
     digitalWrite(11,HIGH);
     Serial2.println("Left");
   }
}
