#include <Servo.h> 
Servo myservo;  // create servo object to control a servo 
                // twelve servo objects can be created on most boards
int pos = 0;    // variable to store the servo position 

//sound
int sound_sensor = A0;
int sound_value;

//Switch
int button = 3;
//LED
int led = 11;
//状態分け LED付いてたらON
int val = 0;
int old_val = 0;
int state = 0;
 
void setup() 
{ 
  //Servo
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
  myservo.write(0);
  
  //Sound
  pinMode(sound_sensor, INPUT);
  Serial.begin(9600);
} 
 
void loop() { 
  //Sound
  sound_value = analogRead(sound_sensor);
  Serial.println(sound_value);
  
  if (state == 1) {
    if (sound_value >= 350) {
    for(pos = 0; pos <= 120; pos += 20) // goes from 0 degrees to 180 degrees 
    {                                  // in steps of 1 degree 
      myservo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(15);                       // waits 15ms for the servo to reach the position 
    }
    delay(2000);
    for(pos = 120; pos>=0; pos-= 20)     // goes from 180 degrees to 0 degrees 
    {                                
      myservo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(15);                       // waits 15ms for the servo to reach the position 
    }
    delay(1000);
    }
  }
  
  //Switch 状態分け LED付いてたら動く
  val = digitalRead(button);
  if ((val == HIGH) && (old_val == LOW)) {
    state = 1 - state;
    delay(10);
  }
  old_val = val;
  if (state == 1) {
    digitalWrite(led, HIGH);
  } else {
    digitalWrite(led, LOW);
  }
} 

