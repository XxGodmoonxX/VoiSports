//sound
int sound_sensor = A0;
int sound_value;

//DCMotor
int motor = 11;

//Switch
int button = 2;
//LED
int led = 13;
//状態分け LED付いてたらON
int val = 0;
int old_val = 0;
int state = 0;

void setup() {
  //DCmotor
  pinMode(motor, OUTPUT);
  
  //Sound
  pinMode(sound_sensor, INPUT);
  Serial.begin(9600);
  
  //Switch
  pinMode(button, INPUT);
  //LED
  pinMode(led, OUTPUT);
}

void loop() {
  //Sound
  sound_value = analogRead(sound_sensor);
  Serial.println(sound_value);
  
  //DCMotor
  //LEDついてたら動く
  if (state == 1) {
    if (sound_value > 70) {
    digitalWrite(motor, HIGH);
    } else {
    digitalWrite(motor, LOW);
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
