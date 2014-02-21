import pandas
import pandasql

def avg_min_temperature(filename):
    '''
    This function should run a SQL query on a dataframe of
    weather data. More specifically you want to find the average
    minimum temperature on rainy days where the minimum temperature
    is greater than 55 degrees.
    
    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be equal to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply 
    where maxtempi = 76.
    
    You can see the weather data that we are passing in below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)

    #q = "SELECT AVG(mintempi) from weather_data WHERE cast(rain as integer) = 1 AND mintempi > 55;"
    q = "SELECT AVG(mintempi) from weather_data WHERE cast(rain as integer) = 1 AND mintempi > 55;"

    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends

local_dir = "/Users/johnmorgan/datasci/hw2"
input_file = "%s/weather_underground.csv" % local_dir
print avg_min_temperature(input_file)