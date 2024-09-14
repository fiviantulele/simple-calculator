import streamlit as st

def calculator():
    """A simple calculator function using Streamlit."""

    st.title("Simple Calculator")

    # Create a dropdown for operation selection
    operation = st.selectbox("Choose an operation:", 
                              ["Addition", "Subtraction", "Multiplication", "Division"])

    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    if operation == "Addition":
        result = num1 + num2
        st.write(f"{num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"{num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"{num1} * {num2} = {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero.")
        else:
            result = num1 / num2
            st.write(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
