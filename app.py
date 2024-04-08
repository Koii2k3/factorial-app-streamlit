import streamlit as st
from factorial import fact

def main():
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number (0-999)", min_value=0, max_value=999)
    if st.button("Calculate"):
        res = fact(number)
        st.write(f"Factorial of {number} is {res}")
        st.balloons()
        
if __name__ == "__main__":
    main()