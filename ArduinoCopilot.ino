#include <Wire.h>
#include "ArduinoCommunication.h"

#include <Temperature_LM75_Derived.h>
#define TCA_ADDRESS  0x70 // I2C address of the TCA9548A
#define TCA9548A_CHANNEL_0    0

struct TemperatureSensor {
	int address;
	Generic_LM75 sensor;
};

TemperatureSensor tempSensors[] = {
	{0x40, Generic_LM75 (0x40)},
	{0x41, Generic_LM75 (0x41)},
	{0x42, Generic_LM75 (0x42)},
	{0x43, Generic_LM75 (0x43)},
	{0x44, Generic_LM75 (0x44)},
	{0x45, Generic_LM75 (0x45)},
	{0x46, Generic_LM75 (0x46)},
	{0x47, Generic_LM75 (0x47)},
	{0x48, Generic_LM75 (0x48)},
	{0x49, Generic_LM75 (0x49)},
	{0x4A, Generic_LM75 (0x4A)},
	{0x4B, Generic_LM75 (0x4B)},
	{0x4C, Generic_LM75 (0x4C)},
	{0x4D, Generic_LM75 (0x4D)},
	{0x4E, Generic_LM75 (0x4E)},
	{0x4F, Generic_LM75 (0x4F)},
	{0x50, Generic_LM75 (0x50)},
	{0x51, Generic_LM75 (0x51)},
	{0x52, Generic_LM75 (0x52)},
	{0x53, Generic_LM75 (0x53)},
	{0x54, Generic_LM75 (0x54)},
	{0x55, Generic_LM75 (0x55)},
	{0x56, Generic_LM75 (0x56)},
	{0x57, Generic_LM75 (0x57)},
	{0x58, Generic_LM75 (0x58)},
	{0x59, Generic_LM75 (0x59)},
	{0x5A, Generic_LM75 (0x5A)},
	{0x5B, Generic_LM75 (0x5B)},
	{0x5C, Generic_LM75 (0x5C)},
	{0x5D, Generic_LM75 (0x5D)},
	{0x5E, Generic_LM75 (0x5E)},
	{0x5F, Generic_LM75 (0x5F)}};

void setup() { 
	Serial.begin(115200); 
	Serial.setTimeout(5); 

	Wire.begin(); // join i2c bus (address optional for master)

	StaticJsonDocument<200> doc = readSerial();
	if (!doc.isNull()) { 
		executeJsonCommand(doc);
	}else{
		Serial.println("Setup failed");
	}
} 

void loop() { 
	while (!Serial) {
		// Wait for serial input

	}; 

	//Serial.println("Temperature: DUMMYVALUE°C");
	if (Serial.available()>0) {
		StaticJsonDocument<200> doc = readSerial();
		if (!doc.isNull()) { 
			executeJsonCommand(doc);
		}else{
			Serial.println("Error parsing JSON");
		}
	}
} 

/**
 * Toggles the pin based on the type of command
 * @param doc The JSON document
 * @return void
 * 		- If the command is "ON", the pin is turned on with the specified PWM value
 * 		- If the command is "OFF", the pin is turned off
 * 		- If the command is invalid, the function prints an error message
*/
void togglePin(StaticJsonDocument<200> doc){

	int pin = doc["pin_num"].as<int>(); // Access the value associated with the key "pin"
	int pwmVal = doc["pwm_val"].as<int>(); // Access the value associated with the key "value"

	Generic_LM75 temp_sensor = getTemperatureSensor(doc["temp_adrr"].as<int>());
	int temp = 0;

	for (int channel = 0; channel < 4; channel++) {
        selectChannel(channel); // Select channel
        // Communicate with devices on the selected bus
		// int temp = temp_sensor.readTemperatureC();
        // delay(100); // Delay for stability
    }

	Serial.println("Temperature: " + String(temp) + "°C");

	if (strcmp(doc["type"], "ON") == 0) { 
		analogWrite(pin, pwmVal);		
		Serial.println("Pin " + String(pin) + " turned ON with PWM value of " + String(pwmVal));
		}else if(strcmp(doc["type"], "OFF") == 0) {
		analogWrite(pin, 0);		
		Serial.println("Pin " + String(pin) + " turned OFF");
		}else{
		Serial.println("Toggling failed.");
		} 
}

/**
 * Sets up the pins based on the JSON document
 * @param doc The JSON document
 * @return void
 * 		- If the command is "Setup", the pins are set up as OUTPUT
 * 		- If the command is invalid, the function prints an error message
*/
void setupPins(StaticJsonDocument<200> doc){
	JsonObject pwmPinValues = doc["pwm_pin_val"]; // Access the nested JSON object

	// Iterate over the pwmPinValues
	for (JsonPair pin : pwmPinValues) {
		int value = pin.value(); 
		pinMode(value, OUTPUT);
		analogWrite(value, 0);	
			
		Serial.println("Pin: " + String(value) + " as OUTPUT.");
		}	
}

void setupTemperatureSensors(StaticJsonDocument<200> doc){
	JsonObject temperatureSensors = doc["temp_adrr"]; // Access the nested JSON object

	// Iterate over the LED TemperatureSensors
	for (JsonPair sensor : temperatureSensors) {
		
		}
}

/**
 * Executes the JSON command
 * @param doc The JSON document
 * @return void
 * 		- If the command is "Setup", the pins are set up as OUTPUT
 * 		- If the command is "ON", the pin is turned on with the specified PWM value
 * 		- If the command is "OFF", the pin is turned off
 * 		- If the command is invalid, the function prints an error message
*/
void executeJsonCommand(StaticJsonDocument<200> doc){
	if (strcmp(doc["type"], "Setup") == 0) {
		// Setup
		setupPins(doc);
		setupTemperatureSensors(doc);
	}else if(strcmp(doc["type"], "ON") == 0 || strcmp(doc["type"], "OFF") == 0) {
		// Toggling
    	togglePin(doc);
	}else{
		String type = doc["type"];
		Serial.println("Invalid command. Execution of " + type + " failed.");
	}
}

Generic_LM75 getTemperatureSensor(int address){
	for (int i = 0; i < sizeof(tempSensors); i++){
		if (tempSensors[i].address == address){
			return tempSensors[i].sensor;
		}
	}
}

void selectChannel(uint8_t channel) {
    Wire.beginTransmission(TCA_ADDRESS);
    Wire.write(1 << channel); // Select the channel
    Wire.endTransmission();
}