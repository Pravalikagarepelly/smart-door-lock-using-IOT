void setup() {
Serial.begin(9600); // Start serial communication 
pinMode(7, OUTPUT); // Green LED 
pinMode(8, OUTPUT); // Red LED
}
void loop() {
if (Serial.available()) {
char command = Serial.read(); 
if (command == 'G') {
digitalWrite(7, HIGH); // Green ON 
digitalWrite(8, LOW); // Red OFF
} else if (command == 'R') { 
digitalWrite(7, LOW); // Green OFF 
digitalWrite(8, HIGH); // Red ON
}
}
}
