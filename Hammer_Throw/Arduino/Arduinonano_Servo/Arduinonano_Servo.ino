//Servo
#include <Servo.h>
Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards
int pos = 0;    // variable to store the servo position
int servo = 9;

//sound
int sound_sensor = A0;
int sound_value;

int old_1_sound_value;
int old_2_sound_value;

//Switch
int button = 3;
//LED
int led = 11;
//状態分け LED付いてたらON
int val = 0;
int old_val = 0;
int state = 0;

//ダミー
int dummy = 5;

void setup()
{
  //Servo
  myservo.attach(servo);  // attaches the servo on pin 9 to the servo object
  myservo.write(0);

  //Sound
  pinMode(sound_sensor, INPUT);
  Serial.begin(9600);
}

void loop() {
  //Sound
  sound_value = analogRead(sound_sensor);
  Serial.println(sound_value);

//  if (state == 1) {
    if (sound_value >= 370) {
      for (pos = 0; pos <= 140; pos += 20) // goes from 0 degrees to 180 degrees
      { // in steps of 1 degree
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      delay(2000);
      for (pos = 140; pos >= 0; pos -= 20) // goes from 180 degrees to 0 degrees
      {
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      delay(2000);
    }
//  }
  
  //ダミー、モバイルバッテリーをONにしておく用
  digitalWrite(dummy, HIGH);
  
  //3連続でその値を超えたら？
  old_2_sound_value = old_1_sound_value; //1つ前の音量を2つ前の音量に 1→2
  old_1_sound_value = sound_value; //今の音量を1つ前の音量に 0→1

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

