import streamlit as st
import requests
import datetime as dt

st.set_page_config(
    page_title="Global Clock",
    page_icon="icon.png",
    menu_items={
        "About":"Get real-time updates on the date, time, and day for any timezone. Our user-friendly interface makes it simple to stay on top of time around the world."
    }   
)

st.write("<h2 style='color:#FF4500;'>Your Gateway to Global World Clock!</h2>",unsafe_allow_html=True)

timezones=requests.get("https://timeapi.io/api/TimeZone/AvailableTimeZones")
data=timezones.json()
user_timezone=st.selectbox("Choose Your Time Zone",data)

btn=st.button("Get Time")
if btn:
    try:
        fetch_timezone=requests.get(f"https://timeapi.io/api/Time/current/zone?timeZone={user_timezone}")
        main_data=fetch_timezone.json()

        time=f"{main_data['hour']}:{main_data['minute']}:{main_data['seconds']}"
        formatted_time=dt.datetime.strptime(time,"%H:%M:%S").strftime("%I:%M:%S %p")
        date=f"{main_data['day']}-{main_data['month']}-{main_data['year']}"
        formatted_date=dt.datetime.strptime(date,"%d-%m-%Y").strftime("%d-%m-%Y")

        st.write(f"<h3 style=font-size:32px;><span style=color:orange;>Date:</span> {formatted_date}</h3>",unsafe_allow_html=True)
        st.write(f"<h3 style=font-size:32px;><span style=color:orange;>Time:</span> {formatted_time}</h3>",unsafe_allow_html=True)
        st.write(f"<h3 style=font-size:32px;><span style=color:orange;>Day:</span> {main_data['dayOfWeek']}</h3>",unsafe_allow_html=True)
    except:
        st.error("Oops! Couldn’t Load")