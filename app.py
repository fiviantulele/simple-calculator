import streamlit as st

def calculator():
    """A more advanced calculator function using Streamlit."""

    st.title("Advanced Calculator")

    # Create a session state to store calculation history
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Create a dropdown for operation selection
    operation = st.selectbox("Choose an operation:", 
                              ["Addition", "Subtraction", "Multiplication", "Division"])

    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero.")
                result = None
            else:
                result = num1 / num2

        if result is not None:
            st.success(f"Result: {result}")
            # Store the calculation result in history
            st.session_state.history.append(f"{num1} {operation} {num2} = {result}")

    # Display calculation history
    if st.session_state.history:
        st.subheader("Calculation History")
        for entry in st.session_state.history:
            st.write(entry)

if __name__ == "__main__":
    calculator()
