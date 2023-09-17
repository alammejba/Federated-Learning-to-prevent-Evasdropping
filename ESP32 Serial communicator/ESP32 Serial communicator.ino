#include <Wire.h>
#include <HMC5883L.h>
#include <TinyGPS++.h>
#include <math.h>

int key = 1;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Serial1.begin(9600);
  Serial3.begin(9600);
  stopp();
  // compassInit();
}

void loop()
{
  while (true)
  {
    Serial3.println('a');
    delay(10000);
    Serial3.println('s');
    delay(2000);
  }
}

void forward()
{
  Serial3.println('a');
}

void rightward()
{
  Serial3.println('c');
}

void leftward()
{
  Serial3.println('d');
}

void stopp()
{
  Serial3.println('s');
}
