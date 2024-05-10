
import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/DeployML/trained_model.sav' , 'rb')) #load is used to load the saved model

# creating a function for prediction

def diabetes_pred(input_data):

    #changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print (prediction)

    if(prediction[0] == 0):
      return 'This person is non-diabetic'
    else:
      return 'This person is diabetic'
  
    
def main():
    
    #giving a title for our webpage
    st.title('Women Diabetes Prediction Web App')
    
    #getting the input data from the user
    
    Pregnancies = st.text_input('Enter the number of pregnancies you have had')
    Glucose = st.text_input('Enter your glucose level')
    BloodPressure = st.text_input('Enter your blood pressure level')
    SkinThickness = st.text_input('Enter skin-thickness')
    Insulin = st.text_input('Enter insulin level')
    BMI = st.text_input('Enter your BMI')
    DiabetesPedigreeFunction = st.text_input('Enter your DiabetesPedigreeFunction')
    Age = st.text_input('Enter your age')
    
    #code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Click for Diabetes Test Result'):
        diagnosis = diabetes_pred([Pregnancies , Glucose ,BloodPressure ,SkinThickness,Insulin , BMI , DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    

    
    
