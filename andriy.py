import streamlit as st
from datetime import datetime

st.title("Part Number Builder")

# Dropdown options and codes
series_options = {
    "Alpha Series": "ALP",
    "Beta Series": "BET",
    "Gamma Series": "GAM"
}

size_options = {
    "Small": "S",
    "Medium": "M",
    "Large": "L"
}

material_options = {
    "Aluminum": "AL",
    "Steel": "ST",
    "Plastic": "PL"
}

color_options = {
    "Red": "R",
    "Blue": "B",
    "Black": "K"
}

# User selections
series = st.selectbox("Select Series", list(series_options.keys()))
size = st.selectbox("Select Size", list(size_options.keys()))
material = st.selectbox("Select Material", list(material_options.keys()))
color = st.selectbox("Select Color", list(color_options.keys()))

# Generate part number
series_code = series_options[series]
size_code = size_options[size]
material_code = material_options[material]
color_code = color_options[color]

part_number = f"{series_code}-{size_code}-{material_code}-{color_code}"

st.markdown("### 🧩 Generated Part Number")
st.code(part_number, language='text')

# Breakdown dictionary for buyer clarity
breakdown = {
    "Series": f"{series_code} = {series}",
    "Size": f"{size_code} = {size}",
    "Material": f"{material_code} = {material}",
    "Color": f"{color_code} = {color}",
}

# st.markdown("### 🔍 Part Number Breakdown")
# st.json(breakdown)

# Initialize part number history in session state
if "part_dict" not in st.session_state:
    st.session_state.part_dict = {}

# Add button
if st.button("➕ Add Part Number"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.part_dict[timestamp] = {
        "Part Number": part_number,
        "Breakdown": breakdown
    }
    st.success("Part number added!")

# Show dictionary of part numbers
if st.session_state.part_dict:
    st.markdown("### 📒 Part Number Dictionary (History)")
    for time, info in st.session_state.part_dict.items():
        st.markdown(f"**{time}**")
        st.code(info["Part Number"])
        st.json(info["Breakdown"])



# & "C:/Users/Pedro Sanhueza/AppData/Local/Programs/Python/Python313/Scripts/streamlit.exe" run "C:/Users/Pedro Sanhueza/OneDrive - RSP Supply/Documents/Script/external projects/Andriy Koval/andriy.py"
# & "C:/Users/Pedro Sanhueza/AppData/Local/Programs/Python/Python313/Scripts/streamlit.exe" run "c:/Users/Pedro Sanhueza/OneDrive - RSP Supply/Documents/Script/external projects/Andriy Koval/andriy.py"