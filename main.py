import requests

api_key='2690b28d6b241854247d17c3662915e5'



def weather_report(user_input):
    weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")

    if(weather_data.json()['cod']=='404'):print("No City Found")
    else:
        '''print(weather_data.json())'''
        weather=weather_data.json()['weather'][0]['main']
        temp=round(weather_data.json()['main']['temp'])
        print(f"The weather in {user_input} is: {weather} and temperature is {temp}°F")


if __name__ == "__main__":
    while True:
        user_input=input("Enter the city name : ")
        if (user_input.lower()=='exit'):
            print("Goodbye!")
            break
        else:
            weather_report(user_input)