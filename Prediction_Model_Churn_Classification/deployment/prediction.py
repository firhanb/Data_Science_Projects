import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import json
import pickle

# Load Files

# Loading Data
# Loading list_num_cols
with open('list_num_cols.txt', 'r') as file_1:
    num_cols = json.load(file_1)

# Loading list_cat_cols_ohe
with open('list_cat_cols_ohe.txt', 'r') as file_2:
    cat_cols_ohe = json.load(file_2)

# Loading list_cat_cols_ord
with open('list_cat_cols_ord.txt', 'r') as file_3:
    cat_cols_ord = json.load(file_3)

# Loading contract_order_for_encoder
with open('contract_order_for_encoder.txt', 'r') as file_4:
    contract_order_for_encoder = json.load(file_4)

# Loading preprocessor
with open('preprocessor.pkl', 'rb') as file_5:
    preprocessor = pickle.load(file_5)

# Loading chi_selector
with open('chi_selector.pkl', 'rb') as file_6:
    chi_selector = pickle.load(file_6)

# Loading anova_selector
with open('anova_selector.pkl', 'rb') as file_7:
    anova_selector = pickle.load(file_7)

# Loading best_pipeline (model)
with open('model.pkl', 'rb') as file_8:
    best_pipeline = pickle.load(file_8)


def run():
  # Membuat Form
  with st.form(key='form_prediksi_churn'):
      gender = st.selectbox('gender:', ['Male', 'Female'])
      SeniorCitizen = st.selectbox('SeniorCitizen:', ['No', 'Yes'])
      Partner = st.selectbox('Partner:', ['No', 'Yes'])
      Dependents = st.selectbox('Dependents:', ['No', 'Yes'])
      st.markdown('---')
      tenure = st.number_input('tenure', min_value=0, max_value=360, value=1, help='Jangka Waktu Berlangganan')
      PhoneService = st.radio('PhoneService:', ['No', 'Yes'])
      MultipleLines = st.radio('MultipleLines:', ['No', 'Yes'])
      InternetService = st.radio('InternetService:', ['No', 'DSL', 'Fiber optic'])
      OnlineSecurity = st.radio('OnlineSecurity:', ['No', 'Yes'])
      OnlineBackup = st.radio('OnlineBackup:', ['No', 'Yes'])
      TechSupport = st.radio('TechSupport:', ['No', 'Yes'])
      StreamingTV = st.radio('StreamingTV:', ['No', 'Yes'])
      StreamingMovies = st.radio('StreamingMovies:', ['No', 'Yes'])
      Contract = st.radio('Contract:', ['Month-to-month', 'One year', 'Two year'])
      PaymentMethod = st.radio('PaymentMethod:', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
      PaperlessBilling = st.radio('PaperlessBilling:', ['No', 'Yes'])
      MonthlyCharges = st.number_input('MonthlyCharges', min_value=-0, max_value=100000, value=0)
      TotalCharges = st.number_input('TotalCharges', min_value=-0, max_value=100000, value=0)
      submitted = st.form_submit_button('Predict')



  new_data = {
      'gender': gender,
      'SeniorCitizen': SeniorCitizen,
      'Partner': Partner,
      'Dependents': Dependents,
      'tenure': tenure,
      'PhoneService': PhoneService,
      'MultipleLines': MultipleLines,
      'InternetService': InternetService,
      'OnlineSecurity': OnlineSecurity,
      'OnlineBackup': OnlineBackup,
      'DeviceProtection': DeviceProtection,
      'TechSupport': TechSupport,
      'StreamingTV': StreamingTV,
      'StreamingMovies': StreamingMovies,
      'Contract': Contract,
      'PaymentMethod': PaymentMethod,
      'PaperlessBilling': PaperlessBilling,
      'MonthlyCharges': MonthlyCharges,
      'TotalCharges': TotalCharges,

  }

  new_data = pd.DataFrame([new_data])
  st.dataframe(new_data)


  if submitted:
      y_pred_inf = best_pipeline.predict(new_data)
      st.write('# Status Churn : ', str(int(y_pred_inf)))
      st.write('0 = Tdk Churn  /  1 = Churn')
