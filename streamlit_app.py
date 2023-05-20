import streamlit as st
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    st.title("Random Number Generator")
    st.write("Click the button below to generate a random number between 1 and 100.")

    if st.button("Generate"):
        random_number = generate_random_number()
        st.write(f"Random number: {random_number}")

if __name__ == '__main__':
    main()
