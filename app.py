import streamlit as st

def main():
    st.title("Mobile Phone Calculator")

    # Initialize session state for the current input and result
    if 'current_input' not in st.session_state:
        st.session_state.current_input = ""
    if 'result' not in st.session_state:
        st.session_state.result = ""

    # Function to update the current input
    def update_input(value):
        st.session_state.current_input += str(value)

    # Function to evaluate the expression
    def evaluate():
        try:
            st.session_state.result = eval(st.session_state.current_input)
        except Exception as e:
            st.session_state.result = "Error"

    # Function to clear the input
    def clear():
        st.session_state.current_input = ""
        st.session_state.result = ""

    # Display the current input and result
    st.write("Current Input: ", st.session_state.current_input)
    st.write("Result: ", st.session_state.result)

    # Create a grid layout for buttons
    cols = st.columns(4)

    # Number buttons
    for i in range(1, 10):
        cols[(i-1) % 3].button(str(i), on_click=update_input, args=(i,))
    
    cols[3].button("0", on_click=update_input, args=(0,))
    cols[3].button("C", on_click=clear)
    
    # Operation buttons
    for op in ['+', '-', '*', '/']:
        cols[3].button(op, on_click=update_input, args=(op,))
    
    cols[3].button("=", on_click=evaluate)

if __name__ == "__main__":
    main()
