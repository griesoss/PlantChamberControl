#include <Wire.h>
#include "ArduinoCommunication.h"

#include <Temperature_LM75_Derived.h>
#define TCA_ADDRESS  0x70 // I2C address of the TCA9548A
#define TCA9548A_CHANNEL_0    0

class TemperatureSensor {
private:
	String name;       // Name of the sensor
    int address;            // Address of the sensor
    Generic_LM75 sensor;    // Instance of the LM75 sensor

   

public:
	// Default constructor
	TemperatureSensor() {}

    // Constructor
    TemperatureSensor(String sensorName, int sensorAddr, Generic_LM75 sensor) : name(sensorName), address(sensorAddr), sensor(sensor)  {}

    // Getter for the address
    int getAddress() const {
        return address;
    }

    // Getter for the name
    String getName() const {
        return name;
    }

    // Method to get the temperature reading from the sensor
    double getTemperature() {
        double temp = sensor.readTemperatureC();
        return temp; // Placeholder return value
    }

    // Other methods and functionalities can be added as needed
};



class DynamicTemperatureSensorArray {
private:
    TemperatureSensor* sensors; // Pointer to array of sensors
    int size; // Current size of the array
    int capacity; // Capacity of the array

public:
    // Constructor
    DynamicTemperatureSensorArray() : sensors(nullptr), size(0), capacity(0) {}

    // Destructor
    ~DynamicTemperatureSensorArray() {
        delete[] sensors; // Free memory
    }

    // Method to add a sensor
    void addSensor(const TemperatureSensor& sensor) {
    if (size >= capacity) {
        // Resize the array if needed
        int newCapacity = (capacity == 0) ? 1 : capacity * 2; // Double the capacity
        TemperatureSensor* newSensors = new TemperatureSensor[newCapacity];

        // Copy existing elements
        for (int i = 0; i < size; ++i) {
            newSensors[i] = sensors[i];
        }

        // Free memory of old array
        delete[] sensors;

        // Update pointers and capacity
        sensors = newSensors;
        capacity = newCapacity;
    }

    // Add the new sensor
    sensors[size++] = sensor;
}


    // Method to get the number of sensors
    int getSize() const {
        return size;
    }

    // Method to access sensors by index
    TemperatureSensor& operator[](int index) {
        return sensors[index];
    }
};

DynamicTemperatureSensorArray tempSensors; // Create an instance of the DynamicTemperatureSensorArray class


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

	//delay(5000);
} 

void loop() { 
	while (!Serial) {}; 

	String temperature = measureTemperature();
	Serial.println(temperature);
	
	if (Serial.available()>0) {
		StaticJsonDocument<200> doc = readSerial();
		if (!doc.isNull()) { 
			executeJsonCommand(doc);
		}else{
			Serial.println("Error parsing JSON");
		}
	}
} 

String measureTemperature() {
	StaticJsonDocument<200> doc;
	doc["type"] = "Temperature";
	
	for (int i = 0; i < tempSensors.getSize(); i++) {
		JsonObject temp = doc.createNestedObject(tempSensors[i].getName());
		for (int channel = 0; channel < 4; channel++) {
			selectChannel(channel); // Select channel
			// Communicate with devices on the selected bus
			int temp_val = tempSensors[i].getTemperature();
			//Serial.println("Temperature: " + String(temp_val) + "°C");
			//int temp_val = 20;
			temp["val_" + String(channel)] = temp_val;

			// delay(100); // Delay for stability
		}
	}
	String output;
	serializeJson(doc, output);
	return output;
}


/* Generic_LM75 getTemperatureSensor(int address){
	for (int i = 0; i < sizeof(tempSensors); i++){
		if (tempSensors[i].address == address){
			return tempSensors[i].sensor;
		}
	}
} */


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

	/* Generic_LM75 temp_sensor = getTemperatureSensor(doc["temp_adrr"].as<int>());
	

	for (int channel = 0; channel < 4; channel++) {
        selectChannel(channel); // Select channel
        // Communicate with devices on the selected bus
		// int temp = temp_sensor.readTemperatureC();
        // delay(100); // Delay for stability
    } */

	//int temp = 0;
	//Serial.println("Temperature: " + String(temp) + "°C");

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

/**
 * Sets up the temperature sensors based on the information from the JSON document
 * @param doc The JSON document
 * @return void
*/
void setupTemperatureSensors(StaticJsonDocument<200> doc){
	JsonObject temperatureSensors = doc["temp_addr"]; // Access the nested JSON object
	//connected_TempSensors = 0;
	// Iterate over the LED TemperatureSensors
	for (JsonPair sensor : temperatureSensors) {
		String name = String(sensor.key().c_str()); 
		int address = sensor.value(); 	
		Generic_LM75 temp_sensor = Generic_LM75(address);
		TemperatureSensor tempSensor = TemperatureSensor(name, address, temp_sensor);
		tempSensors.addSensor(tempSensor);
		Serial.println("Temperature sensor: " + name + " at address " + String(address));
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
		//delay(1000);
		setupTemperatureSensors(doc);
		delay(1000);
	}else if(strcmp(doc["type"], "ON") == 0 || strcmp(doc["type"], "OFF") == 0) {
		// Toggling
    	togglePin(doc);
	}else{
		String type = doc["type"];
		//Serial.println(doc);
		Serial.println("Invalid command. Execution of " + type + " failed.");
	}
}



void selectChannel(uint8_t channel) {
    Wire.beginTransmission(TCA_ADDRESS);
    Wire.write(1 << channel); // Select the channel
    Wire.endTransmission();
}



		