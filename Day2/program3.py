from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    Description: this function is used to get weather information for a city.
    
    Arguments:
        param1 (city): city name for which the weather information is required.
        
    Returns: Weather information of a selected if available.
    """
    
    # temperatrue data
    data = {
        'pune': 'rainy with 25 degree celsius',
        'mumbai': 'sunny with 30 degree celsius',
        'delhi': 'cloudy with 20 degree celsius',
    }
    
    # get the city weather
    if city in data:
        return data[city.lower()]
    
    # city does not exist
    return f'weather information for {city} is not available'

 # note - since get_weather is tool it cannot be called directly.
 # print(get_weather('karad')) # this will give error
 
# get the information/metadata of a tool
print(get_weather)
 
# Invoke or execute the tool
print(get_weather.invoke({'city': 'karad'})) # this will give the weather information for pune