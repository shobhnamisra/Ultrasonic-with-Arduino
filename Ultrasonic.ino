
const int triggerPin = 7;
const int inputPin = 8;

void setup() {
  pinMode(inputPin, INPUT);
  pinMode(triggerPin, OUTPUT);
  // initialize serial communication:
  Serial.begin(9600);
}

void loop()
{
  long duration, cm;

  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(triggerPin, LOW);

  // duration is the duration of time between sending of signal and receiving of signal
  
  duration = pulseIn(inputPin, HIGH);

  // convert the time into a distance
  cm = microsecondsToCentimeters(duration);
  
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();
  
  delay(100);
}


long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}
