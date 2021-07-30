import streamlit as st
import datetime
import requests
import urllib.parse

'''
# TaxiFareModel front
'''

pickup_location = st.sidebar.text_input("Pickup Location")
dropoff_location = st.sidebar.text_input("Dropoff Location")

url_map_pickup = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(pickup_location) +'?format=json'
url_map_dropoff = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(dropoff_location) +'?format=json'

response_pickup_location = requests.get(url_map_pickup).json()
response_dropoff_location = requests.get(url_map_dropoff).json()

d = st.sidebar.date_input(
    "Select date",
    datetime.date(2021, 7, 30))

t = st.sidebar.time_input('Select time', datetime.time(14, 00))

pickup_datetime = datetime.datetime.combine(d, t)

st.write('Datetime: ', pickup_datetime)

p_long = response_pickup_location[0]["lon"]

st.write('Pickup Longitude is ', p_long)

p_lat = response_pickup_location[0]["lat"]

st.write('Pickup Latitude is ', p_lat)

d_long = response_dropoff_location[0]["lon"]

st.write('Dropoff Longitude is ', d_long)

d_lat = response_dropoff_location[0]["lat"]

st.write('Dropoff Latitude is ', d_lat)

p_count = int(st.sidebar.number_input('Passenger Count'))

st.write('Passenger Count is ', p_count)

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

params = {
        "key": str(pickup_datetime) + '.000000119',
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": p_long,
        "pickup_latitude": p_lat,
        "dropoff_longitude": d_long,
        "dropoff_latitude": d_lat,
        "passenger_count": p_count
        }

response = requests.get(
    url,
    params=params
).json()

st.write('The prediction is $', round(response['prediction'],2))
