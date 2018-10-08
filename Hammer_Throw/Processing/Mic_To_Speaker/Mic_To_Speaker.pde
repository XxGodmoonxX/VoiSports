import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;

Minim minim;
AudioOutput out;
LiveInput in;

void setup(){
  size(512, 200);
  minim = new Minim(this);
  out = minim.getLineOut();
  AudioStream inputStream = minim.getInputStream(
                            out.getFormat().getChannels(),
                            out.bufferSize(),
                            out.sampleRate(),
                            out.getFormat().getSampleSizeInBits());
  in = new LiveInput(inputStream);
  in.patch(out);
}

void draw(){
  background(0);

  stroke(255);
  strokeWeight(1);
  for(int i = 0; i < out.bufferSize() - 1; i++){
    line(i, 50 + out.left.get(i) * 50, i + 1, 50 + out.left.get(i + 1) * 50);
    line(i, 150 + out.right.get(i) * 50, i + 1, 150 + out.right.get(i + 1) * 50);
  }
}