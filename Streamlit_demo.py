#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import plotly as py
import plotly.io as pio
from plotly import graph_objects as go

import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data




def main():
    
    create_usertable()
    add_userdata('Vaibhav',make_hashes('zs12345'))
    add_userdata('Adnan',make_hashes('zs12345'))
    add_userdata('Matt',make_hashes('zs12345'))
    add_userdata('Sagar',make_hashes('zs12345'))
    add_userdata('Keith',make_hashes('zs12345'))
    
    st.beta_set_page_config(page_title="SML Dashboard", page_icon=None, layout='wide', initial_sidebar_state='auto')
    st.title("Social Media Listening Dashboard")
    st.sidebar.title("Login page")

    st.markdown("This application is a Streamlit dashboard used "
                "for Social Media Listening")
    st.sidebar.markdown("Please select Login and enter username & password")

    st.header("Login Status")

    menu = ["Home","Login"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        st.info("To access the dashboard select the login option in the sidebar")

    elif choice == "Login":
#         st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
#             if password == '12345':    
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                st.success("Logged in as {}".format(username))

                labels =  ["People who like streamlit", "People who don't know about streamlit"]
                values = [80, 20]


                # pull is given as a fraction of the pie radius
                fig = go.Figure(data=[go.Pie(labels=labels, values=values,textinfo='label+percent',
                                             insidetextorientation='radial', pull=[0, 0, 0.2, 0] #,hole = 0.2
                                            )])


                fig.update_layout(
                    title_text="Demo streamlit app")


                st.plotly_chart(fig, sharing='streamlit')

            else:
                st.warning("Incorrect Username/Password")
                
if __name__ == '__main__':
    main()




