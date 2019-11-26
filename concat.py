import pandas as pd

india_weather = pd.DataFrame({
    "city" : ["mumbai" , "delhi" , "banglore"],
    "temp" : [32,45,30],
    "humidity" : [80,60,78]
})

print(india_weather.head())

us_weather = pd.DataFrame({
    "city" : ["new York" , "chicago" , "orlando"],
    "temp"  : [23,14,35],
    "humidity" : [60,65,75]
})

print("\n")

print(us_weather.head())
print("\n")

data = pd.concat([india_weather , us_weather] , ignore_index=True )
print(data )

print("\n")

data = pd.concat([india_weather , us_weather] ,keys=["India",  "US"])
print(data )

