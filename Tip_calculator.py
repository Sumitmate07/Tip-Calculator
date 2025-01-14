#print("Welcome to the Tip Calculator")
#bill=float(input("What's was the total bill?"))
#tip=int(input("How much tip would you like to give?10,12 or 20 "))
#people=int(input("How many people to split the bill?"))
#bill_with_tip=tip/100*bill+bill
#bill_per_person=bill_with_tip/people
#final_amount=round(bill_per_person,2)
#print(f'Each person should pay:{final_amount}')
import streamlit as st

# Title of the app
st.title("Tip Calculator💰")

# Inputs from the user
bill = st.number_input("Enter the total bill amount:", min_value=0.0, format="%.2f")
tip_percentage = st.slider("Select tip percentage:", 0, 100, 10)
people = st.number_input("How many people to split the bill?", min_value=1, value=1)

# Calculate the bill with the tip
bill_with_tip = (tip_percentage / 100) * bill + bill

# Calculate the amount each person should pay
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

if st.button("Calculate"):
    st.success(f"Each person should pay: {final_amount}")

# Optional: Add some styling to the output
st.markdown(
    """
    <style>
    [data-testid="stSuccess"] {
        background-color: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
    }
    </style>
    """,
    unsafe_allow_html=True
)
