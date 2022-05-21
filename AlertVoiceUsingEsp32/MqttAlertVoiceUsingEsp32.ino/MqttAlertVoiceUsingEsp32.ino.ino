//NodeMCU ISD1820 
//written by RoboGi
#include <WiFi.h>
#include <PubSubClient.h>

//define pin for Arduino IDE
#define PLAY_E 4 //NodeMCU pin d1
#define REC 5    //NodeMCU pin d4
#define PLAY_L 2 //NodeMCU pin d2

int recordTime ;
const char* ssid = "********"; // Enter your WiFi name
const char* password =  "********"; // Enter WiFi password
const char* mqttServer = "192.168.0.104";
const char *topic = "foo_topic";
const int mqttPort = 9001;
const char* MQTT_SERIAL_RECEIVER_CH ="foo_topic";
const char* mqtt_server = "192.168.0.104";

WiFiClient wifiClient;
PubSubClient client(wifiClient);

void setup_wifi() {
    delay(10);
    // We start by connecting to a WiFi network
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    randomSeed(micros());
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}



void setup() 
{
  //Set all the pin OUTPUT (we must send out a signal to the ISD1820)
  pinMode(REC,OUTPUT);
  pinMode(PLAY_L,OUTPUT);
  pinMode(PLAY_E,OUTPUT);
  Serial.begin(115200); 
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
 // client.setServer(mqttServer, mqttPort);
  while (!client.connected()) {
    Serial.println("Connecting to MQTT…");
    if (client.connect("ESP32Client", "", "" )) {
        Serial.println("connected to MQTT");
        client.subscribe(topic);
       // Serial.print(message);
    } else {
        Serial.print("failed to connect");
        Serial.print(client.state());
        delay(2000);
   }
}
}

void callback(char *topic, byte *payload, unsigned int length) {
 Serial.print("Message arrived in topic: ");
 Serial.println(topic);
 Serial.print("Message:");
 if(length>0){
  playSignal ();
 }
 for (int i = 0; i < length; i++) {
     Serial.print((char) payload[i]);
 }
 Serial.println();
 Serial.println("-----------------------");
}


void loop() {
  client.loop();
    while (Serial.available() > 0) {
          char C = (char)Serial.read();
          Serial.println(C);
          
            if(C =='p' || C =='P'){
              Serial.println(C);
            playSignal ();
            break; 
            }
               
            else if(C =='r' || C =='R'){
              Serial.println(C);
              record(3000);              
            }
             
            else if(C =='l' || C =='L'){
              Serial.println(C);
              playSignal_L (1000); //for example if I have my recording is 3 seconds long with this instruction I will only produce it for a second
            }             
           
     
    }// wihile

    //Serial.println("**** R or r = Record ; P or p play****");

  delay(1000);
}
 
void record(int t) //t is the recording time (us)
{
      recordTime =t;
      digitalWrite(REC, HIGH); //For the time that the pin is set to high the module will record a sound (max 10 sec)
      Serial.println("Recording started");
      delay(t);
      digitalWrite(REC, LOW);
      Serial.println("Recording Stopped ");
}

void playSignal ()
{
   digitalWrite(PLAY_E, HIGH); //If the pin is placed high it will play back all the recorded sound (50 us signal is sufficient for the reproduction of the recorded sound)
  delay(50);
  digitalWrite(PLAY_E, LOW);  
    Serial.println("Playbak Started"); 
    if(recordTime == 0)
    {
      delay(recordTime + 5000);
    } 
    else
    {
      delay(recordTime);
    }
  Serial.println("Playbak Ended");
  
}

void playSignal_L (int l) //l is how long the recorded sound has to be produced (in us)
{
     digitalWrite(PLAY_L, HIGH); //For the time that the pin is set to high the module will produce the recorded sound
     Serial.println("Playbak L Started");  
     delay(l);
     digitalWrite(PLAY_L, LOW);
     Serial.println("Playbak L Ended");    
}
