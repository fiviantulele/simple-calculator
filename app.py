import streamlit as st

# Memory storage for the calculator
memory = 0

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error"

def update_memory(value):
    global memory
    memory = value

def recall_memory():
    return memory

# Streamlit UI
st.title("Streamlit Calculator with Memory Functions")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on user input
if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)

# Display result
st.write("Result: ", result)

# Memory function buttons
if st.button("M+"):
    update_memory(result)
    st.write("Value stored in memory: ", memory)

if st.button("MR"):
    st.write("Recalled from memory: ", recall_memory())

if st.button("MC"):
    update_memory(0)
    st.write("Memory cleared")

# Option to clear result
if st.button("Clear"):
    st.write("Result cleared")
