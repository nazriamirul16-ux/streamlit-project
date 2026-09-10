import streamlit as st

# 1. Button Example
st.title("Button Example")
matricNum = st.text_input("Your Matric Number:")
if st.button("Submit"):
    st.success(f"Your Matric Number is {matricNum}")

st.write("---")

# 2. Checkboxes Example
st.title("CheckBoxes Example")
agree = st.checkbox("I agree")
disagree = st.checkbox("I Disagree")

if agree:
    st.write("You agreed!")
elif disagree:
    st.write("You disagreed!")

st.write("---")

# 3. Radio Buttons Example
st.title("Radio Button Example")
choice = st.radio("Choose one:", ["Option A", "Option B", "Option C"])
st.write("You selected:", choice)

st.write("---")

# 4. Selectbox (Dropdown) Example
st.title("Dropdown Example")
fruit = st.selectbox("Pick a fruit:", ["Apple", "Banana", "Cherry"])
st.write("You chose:", fruit)
