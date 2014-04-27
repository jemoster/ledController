#define GREEN 2
#define RED 3
#define BLUE 4

int red = 0;
int green = 0;
int blue = 0;

void setup() {
  
    pinMode(RED, OUTPUT); 
    pinMode(GREEN, OUTPUT); 
    pinMode(BLUE, OUTPUT); 
    
    setColor(RED, red);
    setColor(GREEN, green);
    setColor(BLUE, blue);
    
    Serial.begin(57600);
}

void loop() {
      
    if(Serial.find("S")) {
      Serial.write('S');
      setColor(RED, Serial.parseInt());
      setColor(GREEN, Serial.parseInt());
      setColor(BLUE, Serial.parseInt());
      printColors();
    }
}

void printColors() {
    Serial.print("R=");
    Serial.print(red);
    Serial.print("G=");
    Serial.print(green);
    Serial.print("B=");
    Serial.println(blue); 
}

void setColor( int pin, int brightness ) {
  brightness = brightness>255 ? 255 : (brightness<0 ? 0 :brightness);
  
  switch (pin) {
    case RED:
      red = brightness;
      analogWrite(RED, red);
      break;
    case GREEN:
      green = brightness;
      analogWrite(GREEN, green);
      break;
    case BLUE:
      blue = brightness;
      analogWrite(BLUE, blue);
      break;
    default:
      Serial.println("INVALID PIN");
  }
}
