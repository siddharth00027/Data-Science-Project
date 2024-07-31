import streamlit as st
import util

def main():
    st.title('Home Price Prediction')

    # Load saved artifacts
    util.load_saved_artifacts()

    # User input
    location = st.selectbox('Select Location', util.get_location_name())
    total_sqft = st.number_input('Total Square Feet', min_value=0.0)
    bhk = st.number_input('BHK', min_value=0)
    bath = st.number_input('Bath', min_value=0)

    if st.button('Predict'):
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        st.write(f'Estimated Price: ₹{estimated_price} Lac')

if __name__ == '__main__':
    main()