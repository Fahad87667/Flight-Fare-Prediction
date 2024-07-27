import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load(open(r"noteboook\flight.joblib", "rb"))

def convert_airline_to_numerical(airline):
    if airline == 'Jet Airways':
        return 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    elif airline == 'IndiGo':
        return 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0
    elif airline == 'Air India':
        return 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0
    elif airline == 'Multiple carriers':
        return 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0
    elif airline == 'SpiceJet':
        return 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
    elif airline == 'Vistara':
        return 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
    elif airline == 'GoAir':
        return 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0
    elif airline == 'Multiple carriers Premium economy':
        return 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0
    elif airline == 'Jet Airways Business':
        return 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    elif airline == 'Vistara Premium economy':
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0
    elif airline == 'Trujet':
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
    else:
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

def convert_source_to_numerical(source):
    if source == 'Delhi':
        return 1, 0, 0, 0
    elif source == 'Kolkata':
        return 0, 1, 0, 0
    elif source == 'Mumbai':
        return 0, 0, 1, 0
    elif source == 'Chennai':
        return 0, 0, 0, 1
    else:
        return 0, 0, 0, 0

def convert_destination_to_numerical(destination):
    if destination == 'Cochin':
        return 1, 0, 0, 0, 0
    elif destination == 'Delhi':
        return 0, 1, 0, 0, 0
    elif destination == 'New_Delhi':
        return 0, 0, 1, 0, 0
    elif destination == 'Hyderabad':
        return 0, 0, 0, 1, 0
    elif destination == 'Kolkata':
        return 0, 0, 0, 0, 1
    else:
        return 0, 0, 0, 0, 0

def predict_flight_price():
    st.title("Flight Price Prediction")

    # Date_of_Journey
    date_dep = st.date_input("Departure Date and Time", pd.to_datetime("today"))
    Day_of_Journey = date_dep.day
    Month_of_Journey = date_dep.month

    # Departure
    Dep_hr = st.slider("Departure Hour", 0, 23, 12)
    Dep_min = st.slider("Departure Minute", 0, 59, 30)

    # Arrival
    date_arr = st.date_input("Arrival Date and Time", pd.to_datetime("today"))
    Arrival_hr = st.slider("Arrival Hour", 0, 23, 18)
    Arrival_min = st.slider("Arrival Minute", 0, 59, 0)


    # Duration
    Duration_hrs = abs(Arrival_hr - Dep_hr)
    Duration_mins = abs(Arrival_min - Dep_min)

    # Total Stops
    Total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])

    # Airline
    Airline = st.selectbox("Airline", ["Jet Airways", "IndiGo", "Air India", "Multiple carriers", "SpiceJet", "Vistara", "GoAir",
                                       "Multiple carriers Premium economy", "Jet Airways Business", "Vistara Premium economy", "Trujet"])

    # Source
    Source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai"])

    # Destination
    Destination = st.selectbox("Destination", ["Cochin", "Delhi", "New_Delhi", "Hyderabad", "Kolkata"])

    # Convert categorical variables to numerical
    Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business, Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara, Vistara_Premium_economy = convert_airline_to_numerical(Airline)
    s_Chennai, s_Delhi, s_Kolkata, s_Mumbai = convert_source_to_numerical(Source)
    d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata, d_New_Delhi = convert_destination_to_numerical(Destination)

    # Make prediction
    prediction = model.predict([[Total_stops, Day_of_Journey, Month_of_Journey, Dep_hr, Dep_min, Arrival_hr, Arrival_min,
                                 Duration_hrs, Duration_mins, Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
                                 Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara,
                                 Vistara_Premium_economy, s_Chennai, s_Delhi, s_Kolkata, s_Mumbai, d_Cochin, d_Delhi,
                                 d_Hyderabad, d_Kolkata, d_New_Delhi]])

    output = round(prediction[0], 2)

    st.success(f"Your Flight price is Rs. {output}")

if __name__ == "__main__":
    predict_flight_price()
