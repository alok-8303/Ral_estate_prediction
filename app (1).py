import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.sav', 'rb'))

def main():
    st.title("Real Estate Price Predictor")
    st.markdown("Drop in the required Inputs, and we will do the rest.", unsafe_allow_html=True)
    
    # Input sliders
    Distance_to_the_nearest_MRT_station = st.slider("Distance to the Nearest MRT Station (meters)", 0.0, 10000.0)
    Number_of_convenience_stores = st.slider("Number of Convenience Stores", 0, 340)
    Latitude = st.slider("Latitude", -90.0, 90.0)  # Correcting range for latitude
    Longitude = st.slider("Longitude", -180.0, 180.0)  # Correcting range for longitude

    inputs = [[Distance_to_the_nearest_MRT_station, Number_of_convenience_stores, Latitude, Longitude]]

    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(float)
        st.success(f'The predicted House Price per unit area is ${updated_res[0]:.2f}')

if __name__ == '__main__':
    main()
