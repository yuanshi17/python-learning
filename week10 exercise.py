import pandas as pd

#load the weather dataset
weather_df = pd.read_csv('weather.csv')

#display the first 5 rows
weather_df.head(5)
print(weather_df.head(5))

#show basic information
weather_df.info()
print(weather_df.info())

#filter for Philadelphia, PA
Philadelphia_df= weather_df[weather_df['Station.Code']== 'PHL']

#calculate the average temperature
temp_average = Philadelphia_df['Data.Temperature.Avg Temp'].mean()
print("\nAverage Temperature in Philadelphia:", temp_average)

#Max Temp and Mini Temp
hottest_temp = Philadelphia_df['Data.Temperature.Max Temp'].max()
coldest_temp = Philadelphia_df['Data.Temperature.Min Temp'].min()
print("Hottest temperature in Philadelphia:", hottest_temp)
print("Coldest temperature in Philadelphia:", coldest_temp)

#Calculate the total precipitation
ttl_precipitation =Philadelphia_df['Data.Precipitation'].sum()
print("Total precipitation in Philadelphia:", ttl_precipitation)

#number of rainy days (precipitation > 0)
precipitation =(Philadelphia_df['Data.Precipitation']>0).sum()
print("the number of rainy days:", precipitation)

