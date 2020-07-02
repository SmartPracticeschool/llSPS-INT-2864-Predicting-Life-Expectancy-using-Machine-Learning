import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

model=pickle.load(open('model.pkl','rb'))

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(AdultMortality,infantDeaths,Alcohol,percentageExpenditure,HepatitisB,Measles,BMI,underFiveDeaths,Polio,TotalExpenditure,Diphtheria,HIV_AIDS,GDP,Population,thinness_1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling):
    input=np.array([[AdultMortality,infantDeaths,Alcohol,percentageExpenditure,HepatitisB,Measles,BMI,underFiveDeaths,Polio,TotalExpenditure,Diphtheria,HIV_AIDS,GDP,Population,thinness_1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling]]).astype(np.float64)

    prediction=model.predict(input)
    print((prediction))
    return(prediction)



def main():
    st.title("Life Expectancy Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Life Expectancy Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    AdultMortality = st.text_input("AdultMortality","Type Here")
    infantDeaths= st.text_input("infantDeaths","Type Here")
    Alcohol= st.text_input("Alcohol","Type Here")
    percentageExpenditure = st.text_input("percentageExpenditure","Type Here")
    HepatitisB = st.text_input("HepatitisB","Type Here")
    Measles = st.text_input("Measles","Type Here")
    BMI = st.text_input("BMI","Type Here")
    underFiveDeaths = st.text_input("underFiveDeaths","Type Here")
    Polio = st.text_input("Polio","Type Here")
    TotalExpenditure = st.text_input("TotalExpenditure","Type Here")
    Diphtheria= st.text_input("Diphtheria","Type Here")
    HIV_AIDS = st.text_input("HIV_AIDS","Type Here")
    GDP = st.text_input("GDP","Type Here")
    Population = st.text_input("Population","Type Here")
    thinness_1_19_years = st.text_input("thinness_1_19_years","Type Here")
    thinness_5_9_years = st.text_input("thinness_5_9_years","Type Here")
    Income_composition_of_resources = st.text_input("Income_composition_of_resources","Type Here")
    Schooling = st.text_input("Schooling","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(AdultMortality,infantDeaths,Alcohol,percentageExpenditure,HepatitisB,Measles,BMI,underFiveDeaths,Polio,TotalExpenditure,Diphtheria,HIV_AIDS,GDP,Population,thinness_1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling)

    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()