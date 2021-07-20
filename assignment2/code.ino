#include <Servo.h>
Servo s;

int trigg = 3;
int echo = 2;

void setup()
{
  	s.attach(5);
	pinMode(trigg, OUTPUT);
	pinMode(echo, INPUT);
	Serial.begin(9600); 
}

void loop()
{
  s.write(0);
  	digitalWrite(trigg, LOW);
  	digitalWrite(trigg, HIGH);
  	delayMicroseconds(10);
  	digitalWrite(trigg, LOW);
  
  	float dur = pulseIn(echo, HIGH);
  	float dist = (dur/2)*0.034;

  	Serial.println(dist);
  
    if(dist<300) {
      s.write(90);
      delay(1000);
      s.write(0);
    }
  
}