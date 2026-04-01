import streamlit as st
st.title("Calculator")
a=st.number_input("Enter 1st number:")
b=st.number_input("Enter second number:")
#operation
calculate=st.selectbox("select operation:",["Add",'Sub','Mul','Div'])
#button
if st.button('calculate'):
    if calculate=='Add':
        st.success(a+b)
    elif calculate=="Sub":
        st.success(a-b)
    elif calculate=='Mul':
        st.success(a*b)
    elif calculate=='Div':
        st.success(a/b)
    else:
        st.write("not valid input")