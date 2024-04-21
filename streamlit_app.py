import streamlit as st

def find_largest(x, y, z):
    return max(x, y, z)

def main():
    st.title("Find the Largest Among Three Numbers")
    
    st.write("Enter three numbers below:")
    
    num1 = st.number_input("Enter 1st number", value=0)
    num2 = st.number_input("Enter 2nd number", value=0)
    num3 = st.number_input("Enter 3rd number", value=0)
    
    if st.button("Find Largest"):
        largest_no = find_largest(num1, num2, num3)
        st.write(f"The largest number amongst those enterd is: {largest_no}")

if __name__ == "__main__":
    main()
