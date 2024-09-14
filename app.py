import streamlit as st

# Memory storage for the calculator
memory = 0
current_value = ""

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
st.title("Calculator with Memory Functions")

# Display for the calculator
if "display" not in st.session_state:
    st.session_state.display = "0"

def update_display(new_value):
    if st.session_state.display == "0":
        st.session_state.display = new_value
    else:
        st.session_state.display += new_value

def clear_display():
    st.session_state.display = "0"

def calculate_result():
    try:
        st.session_state.display = str(eval(st.session_state.display))
    except:
        st.session_state.display = "Error"

# Calculator display
st.text_input("Display", st.session_state.display, key="display_input", disabled=True)

# Layout for buttons
col1, col2, col3, col4 = st.columns(4)

# First row of buttons
with col1:
    if st.button("MC"):
        update_memory(0)
with col2:
    if st.button("MR"):
        st.session_state.display = str(recall_memory())
with col3:
    if st.button("M+"):
        update_memory(float(st.session_state.display))
with col4:
    if st.button("C"):
        clear_display()

# Second row of buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7"):
        update_display("7")
with col2:
    if st.button("8"):
        update_display("8")
with col3:
    if st.button("9"):
        update_display("9")
with col4:
    if st.button("/"):
        update_display("/")

# Third row of buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("4"):
        update_display("4")
with col2:
    if st.button("5"):
        update_display("5")
with col3:
    if st.button("6"):
        update_display("6")
with col4:
    if st.button("*"):
        update_display("*")

# Fourth row of buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("1"):
        update_display("1")
with col2:
    if st.button("2"):
        update_display("2")
with col3:
    if st.button("3"):
        update_display("3")
with col4:
    if st.button("-"):
        update_display("-")

# Fifth row of buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("0"):
        update_display("0")
with col2:
    if st.button("."):
        update_display(".")
with col3:
    if st.button("="):
        calculate_result()
with col4:
    if st.button("+"):
        update_display("+")

# Memory section
st.write(f"Memory: {memory}")
