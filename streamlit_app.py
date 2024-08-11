import streamlit as st

def app():

  st.title('XXX Trading Platform')
  choice = st.selectbox('Login/Signup', ['Login','Sign Up'])
  if choice == 'Login':
    email = st.text_input('Email Address')
    password = st.text_input('Password',type='password')
    st.button('Login')
  else: 
    username = st.text_input('Username')
    email = st.text_input('Email Address')
    password = st.text_input('Password',type='password')
    st.button('Sign Up')

app
