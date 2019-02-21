import urllib.request,json
from .models import Flight, User
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

api_key = None

base_url = None



def configure_request(app):
    global api_key,base_url
    api_key = app.config['FLIGHT_API_KEY']
    base_url = app.config['FLIGHT_API_BASE_URL']

def get_flight(query):

    get_flight_url ='https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0?api_key={}'.format(api_key)

    with urllib.request.urlopen(get_flight_url) as url:
        get_flight_data = url.read()
        get_flight_response = json.loads(get_flight_data)

        flight_results = None

        if get_flight_response['query']:
            flight_results_list = get_flight_response['query']
            flight_results = process_results(flight_results_list)
            
    return (flight_results)

def process_results(flight_list):
    
    flight_results = []
    for flight in flight_list:
        inboundDate = flight.get('inboundDate')
        cabinClass = flight.get('cabinClass')
        children = flight.get('children')
        infants = flight.get('infants')
        groupPricing = flight.get('groupPricing')
        country = flight.get('country')
        currency = flight.get('currency')
        locale = flight.get('locale')
        originPlace = flight.get('originPlace')
        destinationPlace = flight.get('destinationPlace')
        outboundDate = flight.get('outboundDate')
        adults = flight.get('adults')
        

        flight_object = Flight(inboundDate,cabinClass,children,infants,groupPricing,country,currency,locale,originPlace,destinationPlace,outboundDate,adults)
        

    return flight_results    

   
        
        