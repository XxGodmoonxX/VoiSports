/*
  Controlling a servo position using a potentiometer (variable resistor)
  by Michal Rinott <http://people.interaction-ivrea.it/m.rinott>

  modified on 8 Nov 2013
  by Scott Fitzgerald
  http://www.arduino.cc/en/Tutorial/Knob
*/

//#include <Servo.h>
#include <VarSpeedServo.h>

VarSpeedServo myservo;
//Servo myservo;  // create servo object to control a servo

int potpin = 0;  // analog pin used to connect the potentiometer
int val = 's';    // variable to read the value from the analog pin

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  val = Serial.read();// reads the value of the potentiometer (value between 0 and 1023)
  //Serial.print(val);
  if(val == 'a'){
    myservo.write(175,70,true);
  }else  if(val == 'b'){
    myservo.write(170,70,true);
  }else  if(val == 'c'){
    myservo.write(165,70,true);
  }else  if(val == 'd'){
    myservo.write(160,70,true);
  }else  if(val == 'e'){
    myservo.write(155,70,true);
  }else  if(val == 'f'){
    myservo.write(150,70,true);
  }else  if(val == 'g'){
    myservo.write(145,70,true);
  }else  if(val == 'h'){
    myservo.write(140,70,true);
  }else  if(val == 'i'){
    myservo.write(135,70,true);
  }else  if(val == 'j'){
    myservo.write(130,70,true);
  }else  if(val == 'k'){
    myservo.write(125,70,true);
  }else  if(val == 'l'){
    myservo.write(120,70,true);
  }else  if(val == 'm'){
    myservo.write(115,70,true);
  }else  if(val == 'n'){
    myservo.write(110,70,true);
  }else  if(val == 'o'){
    myservo.write(105,70,true);
  }else  if(val == 'p'){
    myservo.write(100,70,true);
  }else  if(val == 'q'){
    myservo.write(95,70,true);
  }else  if(val == 'r'){
    myservo.write(90,70,true);
  }else  if(val == 's'){
    myservo.write(85,70,true);
  }else  if(val == 't'){
    myservo.write(80,70,true);
  }else  if(val == 'u'){
    myservo.write(75,70,true);
  }else  if(val == 'v'){
    myservo.write(70,70,true);
  }else  if(val == 'w'){
    myservo.write(65,70,true);
  }else  if(val == 'x'){
    myservo.write(60,70,true);
  }else  if(val == 'y'){
    myservo.write(55,70,true);
  }else  if(val == 'z'){
    myservo.write(50,70,true);
  }else  if(val == '0'){
    myservo.write(45,70,true);
  }else  if(val == '1'){
    myservo.write(40,70,true);
  }else  if(val == '2'){
    myservo.write(35,70,true);
  }else  if(val == '3'){
    myservo.write(30,70,true);
  }else  if(val == '4'){
    myservo.write(25,70,true);
  }else  if(val == '5'){
    myservo.write(20,70,true);
  }else  if(val == '6'){
    myservo.write(15,70,true);
  }else  if(val == '7'){
    myservo.write(10,70,true);
  }else  if(val == '8'){
    myservo.write(5,70,true);
  }else  if(val == '9'){
    myservo.write(0,70,true);
  }
  //val = map(val, 0, 180, 0, 180);// scale it to use it with the servo (value between 0 and 180)
  //myservo.write(180); // sets the servo position according to the scaled value
  delay(100);//ここの値を100~300くらいのあたいで試行錯誤すれば動く
}//ターミナルでdoa.pyを実行した後に、ボードへの書き込みを繰り返すと動き出す
