import streamlit as st
import requests
import random

# Length Converter
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Weight Converter
def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462,
        "Ounces": 0.035274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Temperature Converter
def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

# Currency Converter (Using Direct API)
def currency_converter(value, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if to_currency in data["rates"]:
            return value * data["rates"][to_currency]
        else:
            return "Invalid currency code"
    except:
        return "Conversion failed. Try again later."

# UI Start
st.title("🌍 Unit Converter App")

# Sidebar for Selection
option = st.sidebar.selectbox("Choose a conversion type:", ["Length", "Weight", "Temperature", "Currency"])

# Length Conversion
if option == "Length":
    units = ["Meters", "Kilometers", "Miles", "Yards", "Feet"]
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result:.4f} {to_unit}")

# Weight Conversion
elif option == "Weight":
    units = ["Grams", "Kilograms", "Pounds", "Ounces"]
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result:.4f} {to_unit}")

# Temperature Conversion
elif option == "Temperature":
    units = ["Celsius", "Fahrenheit"]
    value = st.number_input("Enter value:", format="%.2f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"Converted Value: {result:.2f}° {to_unit}")

# Currency Conversion
elif option == "Currency":
    currencies = ["USD", "EUR", "GBP", "PKR", "INR", "CAD", "AUD", "JPY", "CNY"]
    value = st.number_input("Enter amount:", min_value=0.0, format="%.2f")
    from_currency = st.selectbox("From Currency:", currencies)
    to_currency = st.selectbox("To Currency:", currencies)
    
    if st.button("Convert"):
        result = currency_converter(value, from_currency, to_currency)
        st.success(f"Converted Value: {result:.2f} {to_currency}" if isinstance(result, float) else result)

# Daily Motivational Quote
st.subheader("💡 Daily Growth Mindset Quote")
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "You can always improve; you are never stuck in one place.",
    "Challenges are what make life interesting; overcoming them is what makes life meaningful.",
    "Hard work and determination can outshine natural talent any day."
]
st.write(f"📢 *{random.choice(quotes)}*")

# Footer with Social Media Icons and Credit
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #333; font-size: 14px;'>
        <p>Development by <strong>Syed zumeer imam</strong></p>
        <a href='https://github.com/mr-anus-alam' target='_blank'>
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' alt='GitHub' style='width:40px; margin: 0 10px;'>
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)