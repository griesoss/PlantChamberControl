import pandas as pd

class TemperatureSet():
    def __init__(self,temperature_data, timestamp):
        """
        Initialize the TemperatureSet object.
        """
        self.temperature_data = temperature_data
        self.timestamp = timestamp


class TemperatureData():
    def __init__(self,name,values):
        """
        Initialize the TemperatureData object.
        """
        self.name = name
        self.values = values
                    
def process_temp_sets(temp_sets):
    """
    Process the temperature set.
    :param temp_data: Temperature data
    """
    columns = ['Time']
    
    for temp_data in temp_sets[0].temperature_data:
        columns.append(temp_data.name)
    
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
        
                
        