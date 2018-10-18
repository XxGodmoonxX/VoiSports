import cc.arduino.*;
import org.firmata.*;

import ddf.minim.*;  //ライブラリのインポート←(1)
import processing.serial.*;

Arduino arduino;

Minim minim;  //Minim用変数←(2)
AudioInput in; //音入力オブジェクト用変数←(2)
float volumeIn;//円の直径になる変数、

void setup() {
  size(250,250);
  minim = new Minim(this);//Minin生成←(3)
  //↓AudioInputオブジェクト生成←(4)
  in = minim.getLineIn(Minim.MONO, 512);
  fill(200,0,0);
     println(Arduino.list());

    arduino = new Arduino(this,"/dev/cu.usbmodem14111", 57600);
 arduino.pinMode(9, Arduino.SERVO);

}

void draw() {
  print(volumeIn);
  background(0);
 //AudioInputオブジェクトから音量を取得、入力値(0から0.5)を0から500に換算←(5)
  volumeIn = map(in.left.level(), 0, 0.5, 0, width*2);
  ellipse(width/2, width/2, volumeIn, volumeIn); //描画
  
  // background(constrain(mouseX / 2, 0, 180));
 
  // Output analog values (PWM waves) to digital pins 9 and 11.
  // Note that only certain Arduino pins support analog output (PWM).
  // See the documentation for your board for details.
 // arduino.analogWrite(9, constrain(mouseX / 2, 0, 180));
//  arduino.analogWrite(11, constrain(180 - mouseX / 2, 0, 180));
  
  if(volumeIn >320){
     //arduino.myservo.write(30); 
   //  arduino.servoWrite(0,180);
     arduino.analogWrite(9, constrain(100 , 0, 360));
     delay(1000);
  }else{
     arduino.analogWrite(9, constrain(0 , 0, 360));

     //arduino.servoWrite(9,180);
 // arduino.digitalWrite(9, Arduino.OUTPUT);  
  //arduino.digitalWrite(9,arduino.LOW);
   // arduino.shock();
  // arduino.pinMode(13,Arduino.OUTPUT);
  }
}

void stop(){
  in.close(); //音声再生オブジェクトを閉じる
  minim.stop();  //Minimオブジェクトをクリア
  super.stop();  //自分でstop()を定義した時、必須
}
