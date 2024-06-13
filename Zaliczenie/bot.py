import tweepy
import requests
import schedule
import time
from datetime import datetime#, timedelta
import pytz
import config

client = tweepy.Client(config.BEARER_TOKEN, config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET, config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET, config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#client.create_tweet(text="Test")

def getWeather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Warsaw,PL&appid={config.OPENWEATHERMAP_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    print("Received data from OpenWeatherMap API: ", data)
    return data
#getWeather()



weather_descriptions = {
    "clear sky": "Czyste niebo",
    "few clouds": "Małe zachmurzenie",
    "scattered clouds": "Rozproszone chmury",
    "broken clouds": "Zachmurzenie",
    "shower rain": "Przelotne opady",
    "rain": "Deszcz",
    "thunderstorm": "Burza",
    "snow": "Śnieg",
    "mist": "Mgła"
}

def descriptionTranslator(description):
    return weather_descriptions.get(description, description)

def weatherTweet():
    weather = getWeather()
    if weather is None:
        return "Nie udało się pobrać danych pogodowych. Spróbuj ponownie później"
    description = weather['weather'][0]['description']
    descriptionPL = descriptionTranslator(description)
    temp = weather['main']['temp']
    temp_min = weather['main']['temp_min']
    temp_max = weather['main']['temp_max']

    current_date = datetime.now().strftime("%d-%m-%Y")

    tweet = (f'Przewidywana prognoza pogody na dzisiaj ({current_date}) w Warszawie🌤🌤🌤:\n'
             f'Opis pogody📝: {descriptionPL}\n'
             f'Przewidywana temperatura🌡: {temp}°C\n'
             f'Minimalna 📉: {temp_min}°C\n'
             f'Maksymalna temperatura📈: {temp_max}°C\n'
             f'Życzę miłego dnia!😄😄')
    print(tweet)
    return tweet
#weatherTweet()

def weatherTweetCreator():
    tweet = weatherTweet()
    try:
        #client.create_tweet(text=tweet)
        print('Tweet: ', tweet, ' został opublikowany.')
    except Exception as e:
        print(f"Failed to post tweet: {e}")
    client.create_tweet(text=tweet)
    #print("Tweet wysłany:", tweet)

def dailyTweetScheduler(run_time):
    #schedule.every().day.at(run_time).do(weatherTweetCreator)
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == run_time:
            weatherTweetCreator()
            time.sleep(10)
        time.sleep(1)

run_time = "07:30"

dailyTweetScheduler(run_time)

