import streamlit as st
from PIL import Image
st.title("Oluwaseun's BMI calculator")
img=Image.open("C:\\Users\\hp\Downloads\\pexels-andres-ayrton-6551234 (1).jpg")
st.image(img)
st.markdown('#### what is BMI?')
st.text("BMI is a measurement of a person\'s leanness or corpulence based on their height and weight, and is intended to quantify tissue mass.\nIt is widely used as a general indicator of whether a person has a healthy body weight for their height."
        "Specifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between.\nThese ranges of BMI vary based on factors")
weight=st.number_input("Enter your weight(in kgs)")
status=st.radio("Enter your preferred format",('cm','m','ft'))
if (status=='cm'):
        height= st.number_input("Enter your height in cm")
        try:
                bmi=weight/(height/100)**2
        except:
                st.text("enter some height value")
elif (status=='m'):
        height=st.number_input("Enter your height in m")
        try:
                bmi=weight/(height)**2
        except:
                st.text("Enter some height value")
else:
        height=st.number_input("Enter your height in ft")
        try:
                bmi=weight/(height*0.3048)**2
        except:
                st.text("Enter some height value")
if(st.button("Calculate")):
        st.text("Your bmi is {}".format(bmi))
        if (bmi < 16):
                st.error("You are extremely underweight")
        elif (bmi >= 16 and bmi < 18.5):
                st.warning("You are underweight")
        elif (bmi >= 18.5 and bmi < 25):
                st.success("Healthy")
        elif (bmi >= 25 and bmi < 30):
                st.warning("You are Overweight")
        elif(bmi>30):
                st.error("You are Extremely Overweight")