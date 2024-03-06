#include "ArduinoCommunication.h"

/**
 * Reads the serial input and parses it into a JSON document
 * @return StaticJsonDocument<200> The JSON document
 *        - If the JSON is valid, the function returns the JSON document
 *        - If the JSON is invalid, the function prints an error message and returns an empty JSON document
 */
StaticJsonDocument<200> readSerial(){
	while (!Serial.available()); 
	String jsonString = Serial.readStringUntil('\n');
	StaticJsonDocument<200> doc; // Create a StaticJsonDocument for parsing JSON with a capacity of 200 bytes
	DeserializationError error = deserializeJson(doc, jsonString); // Parse JSON data

	if (!error) {
		return doc;
		}else{
		Serial.println("Error parsing JSON");
		Serial.println(error.c_str());
		StaticJsonDocument<200> docfail; 
		return docfail;
		}
}