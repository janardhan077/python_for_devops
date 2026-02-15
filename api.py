import requests
api_key = "2BLGYUJDCNWJE96F"
api_url = "https://www.alphavantage.co/"
query = (f"query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}")
print (api_url +query)
def get_api_data ():
    response = requests.get (url =api_url+query)
    print(response.json())
    for key ,value in response.json().items() :
        print (key,value )

get_api_data ( )        
