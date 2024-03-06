#ifndef MyFunctions_h
#define MyFunctions_h

#include <ArduinoJson.h>

/**
 * Reads the serial input and parses it into a JSON document
 * @return StaticJsonDocument<200> The JSON document
 *        - If the JSON is valid, the function returns the JSON document
 *        - If the JSON is invalid, the function prints an error message and returns an empty JSON document
*/
StaticJsonDocument<200> readSerial();

#endif