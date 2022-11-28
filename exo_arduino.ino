int currentPos; //sensor location of exoskeleton
int Enable;     //Enables the shaft of motor (on/off)
int inputA;     //Controlls High oe Low speed
int inputB;     //Controlls right or left movement
int digital_sensor;//one position sensor is digital instead of analog
int sensorThreshold = 100;//value for analog sensor to determine if sensor is tripped

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);                             //begin USB serial connection
  findCurrentPos();                                 //finds current position of the exoskeleton
  if(currentPos != 0){                              //returns the exoskeleton to home starting position
    toHome(0);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  while(!Serial.available());                       //Arduino does nothing until instructions are sent from the PC
  String input = Serial.readString();               //Recieves String data from the PC
  int task = input.substring(0,1).toInt();          //Parses String and converts to int, fist # determines what task is being performed
  int sp = input.substring(1).toInt();              //Parese String and converts to int, second # specifies speed (fast/slow)
  switch(task){                                     //The task sent from the PC directly coorelates to what function the arduino runs
    case 0: toHome(sp); Serial.print("at home position"); break;
    case 1: left1(sp); Serial.print("at left1 position"); break;
    case 2: left2(sp); Serial.print("at left2 position"); break;
    case 3: right1(sp); Serial.print("at right1 position"); break;
    case 4: right2(sp); Serial.print("at right2 position"); break;
    case 5: close(); Serial.print("at closed position"); break;
    case 6: open(); Serial.print("at open position"); break;
  }
}

//Homming function (returns apparatus to center position)
void toHome(int sp){
  switch(currentPos){
    case 0: break;
    case 1:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A0) > sensorThreshold);
      break;
    case 2:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A0) > sensorThreshold);
      break;
    case 3:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A0) > sensorThreshold);
      break;
    case 4:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A0) > sensorThreshold);
      break;
  }
  findCurrentPos();                           //updates current position
}

void left1(int sp){
  switch(currentPos){
    case 0:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A1) > sensorThreshold);
      break;
    case 1:
      break;
    case 2:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A1) > sensorThreshold);
      break;
    case 3:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A1) > sensorThreshold);
      break;
    case 4:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A1) > sensorThreshold);
      break;
  }
  findCurrentPos();                           //updates current position
}

void left2(int sp){
  switch(currentPos){
    case 0:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A2) > sensorThreshold);
      break; 
    case 1:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A2) > sensorThreshold);
      break;
    case 2:
      break;
    case 3:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A2) > sensorThreshold);
      break;
    case 4:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A2) > sensorThreshold);
      break;
  }
  findCurrentPos();                           //updates current position
}

void right1(int sp){
  switch(currentPos){
    case 0:digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A3) > sensorThreshold);
      break; 
    case 1:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A3) > sensorThreshold);
      break;
    case 2:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A3) > sensorThreshold);
      break;
    case 3:
      break;
    case 4:
      digitalWrite(inputB, LOW);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(analogRead(A3) > sensorThreshold);
      break;
  }
  findCurrentPos();                           //updates current position
}

void right2(int sp){
  switch(currentPos){
    case 0: 
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(digitalRead(digital_sensor) == HIGH);
      digitalWrite(Enable, LOW);
      break;
    case 1:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(digitalRead(digital_sensor) == HIGH);
      digitalWrite(Enable, LOW);
      break;
    case 2:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(digitalRead(digital_sensor) == HIGH);
      digitalWrite(Enable, LOW);
      break;
    case 3:
      digitalWrite(inputB, HIGH);
      if(sp == 0){digitalWrite(inputA, LOW);}
      else{digitalWrite(inputA, HIGH);}
      digitalWrite(Enable, HIGH);
      while(digitalRead(digital_sensor) == HIGH);
      digitalWrite(Enable, LOW);
      break;
    case 4:
      break;
  }
  findCurrentPos();                           //updates current position
}

void open(){

}

void close(){ 

}

void findCurrentPos(){
  digitalWrite(Enable, LOW);
  for(int i=0; i<5; i++){
    if(checkSensor(i)){
      currentPos = i;
      return;
    }
  }
  findSensor();
  findCurrentPos();
}

bool checkSensor(int s){
  if(s==4){
    if(digitalRead(digital_sensor) == LOW){
      return true;
    }
  }
  else if (analogRead(s) < sensorThreshold){
    return true;
  }
  else{
    return false;
  }
}

//Slowly moves to the left until at a defined sensor location
void findSensor(){
  digitalWrite(inputA, LOW);
  digitalWrite(inputB, LOW);
  digitalWrite(Enable, HIGH);
  while(analogRead(A0)>sensorThreshold && analogRead(A1)>sensorThreshold && analogRead(A2)>sensorThreshold && analogRead(A3)>sensorThreshold && digitalRead(digital_sensor) == HIGH);
  digitalWrite(Enable, LOW);
}
