import streamlit as st
from datetime import datetime

st.title("Part Number Builder")

# Dropdown options and codes
series_options = {
    "Select a Series...": {"code": "", "price": 0},
    "Alpha Series": {"code": "ALP", "price": 100},
    "Beta Series": {"code": "BET", "price": 150},
    "Gamma Series": {"code": "GAM", "price": 200}
}

size_options = {
    "Select a Size...": {"code": "", "price": 0},
    "Small": {"code": "S", "price": 50},
    "Medium": {"code": "M", "price": 75},
    "Large": {"code": "L", "price": 100}
}

material_options = {
    "Select a Material...": {"code": "", "price": 0},
    "Aluminum": {"code": "AL", "price": 80},
    "Steel": {"code": "ST", "price": 120},
    "Plastic": {"code": "PL", "price": 40}
}

color_options = {
    "Select a Color...": {"code": "", "price": 0},
    "Red": {"code": "R", "price": 25},
    "Blue": {"code": "B", "price": 50},
    "Black": {"code": "K", "price": 75}
}

# User selections
series = st.selectbox("Select Series", list(series_options.keys()))
size = st.selectbox("Select Size", list(size_options.keys()))
material = st.selectbox("Select Material", list(material_options.keys()))
color = st.selectbox("Select Color", list(color_options.keys()))

# Generate part number
part_components = []
total_price = 0

# Only add components if a real option (not placeholder) is selected
if series and series_options[series]["code"]:
    series_code = series_options[series]["code"]
    part_components.append(series_code)
    total_price += series_options[series]["price"]
    
if size and size_options[size]["code"]:
    size_code = size_options[size]["code"]
    part_components.append(size_code)
    total_price += size_options[size]["price"]
    
if material and material_options[material]["code"]:
    material_code = material_options[material]["code"]
    part_components.append(material_code)
    total_price += material_options[material]["price"]
    
if color and color_options[color]["code"]:
    color_code = color_options[color]["code"]
    part_components.append(color_code)
    total_price += color_options[color]["price"]

part_number = "-".join(part_components) if part_components else "No options selected"

st.markdown("### 🧩 Generated Part Number")
st.code(part_number, language='text')

# Breakdown dictionary with prices
breakdown = {}
if series and series_options[series]["code"]:
    series_code = series_options[series]["code"]
    breakdown["Series"] = f"{series_code} = {series} (${series_options[series]['price']})"
if size and size_options[size]["code"]:
    size_code = size_options[size]["code"]
    breakdown["Size"] = f"{size_code} = {size} (${size_options[size]['price']})"
if material and material_options[material]["code"]:
    material_code = material_options[material]["code"]
    breakdown["Material"] = f"{material_code} = {material} (${material_options[material]['price']})"
if color and color_options[color]["code"]:
    color_code = color_options[color]["code"]
    breakdown["Color"] = f"{color_code} = {color} (${color_options[color]['price']})"

# Display breakdown and total price
if breakdown:
    st.markdown("### 📝 Part Breakdown")
    for component, details in breakdown.items():
        st.write(f"**{component}:** {details}")
    st.markdown(f"### 💰 Total Price: ${total_price}")
else:
    st.write("No components selected")
