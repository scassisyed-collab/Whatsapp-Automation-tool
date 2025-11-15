import time
import pyautogui
import streamlit as st  
import pywhatkit as kit
import pandas as pd 


st.title("Whatsapp Automation")
uploadkaren= st.file_uploader("Upload an excel file ",type=["xlsx"])


portfolio_link= st.text_input("enter your portfolio link ")
custom_message= st.text_area("enter your detail message ")

if uploadkaren is not None:
    meradata= pd.read_excel(uploadkaren) 
    show_data= st.dataframe (meradata)

    if st.button("send message "):
        st.write("all contacts are uploaded ")

        for i ,row in meradata.iterrows():
            phone_number=f"+{row["phone"]}"
            message=f"{custom_message},{portfolio_link}"

            kit.sendwhatmsg_instantly(phone_number,message,wait_time=15)

            time.sleep(6)


            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.press("enter")


            






