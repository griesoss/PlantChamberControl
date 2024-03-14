import pandas as pd

class TemperatureSet():
    """
    TemperatureSet class to hold a list of temperature data and the timestamp.    
    """
    def __init__(self,temperature_data, timestamp):
        """
        Initialize the TemperatureSet object.
        :param temperature_data: List of temperature data
        :param timestamp: Timestamp 
        """
        self.temperature_data = temperature_data
        self.timestamp = timestamp


class TemperatureData():
    """
    TemperatureData class to hold the temperature data.
    
    Methods:
        __init__: Initialize the TemperatureData object
    """
    def __init__(self,name,values):
        """
        Initialize the TemperatureData object.
        :param name: Name of LED corresponding to the temperature data
        :param values: List of temperature values
        """
        self.name = name
        self.values = values
                    
def process_temp_sets(temp_sets):
    """
    Refactor the temperature data to a pandas DataFrame.
    :param temp_sets: Temperature data sets
    :return: Pandas DataFrame with the temperature data
    """
    # First column is the time
    columns = ['Time']
    
    # Add the LED names as columns
    for temp_data in temp_sets[0].temperature_data:
        columns.append(temp_data.name)
    
    # Save the data
    data = []
    for temp_set in temp_sets:
        row = [temp_set.timestamp]
        for temp_data in temp_set.temperature_data:            
            index = 0
            sum = 0
            for value in temp_data.values:
                sum = sum + value
                index = index + 1
            row.append(sum/index)
        data.append(row)
    
    return pd.DataFrame(data, columns=columns)           