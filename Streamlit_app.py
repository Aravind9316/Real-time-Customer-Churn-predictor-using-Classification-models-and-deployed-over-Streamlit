import streamlit as st
import numpy as np
import pickle
st.set_option('deprecation.showfileUploaderEncoding', False)
model = pickle.load(open('AdaBoost_final.pkl', 'rb'))

def main():
    st.title('Customer Attrition Classification on Telco Sector')
    st.write('This model will help us to indentify if the Customer will Churn or Not')

    # Input
    st.write('Gender: Male - 0, Female - 1')
    gender = st.number_input('Gender', 0, 1)

    st.write('Senior Citizen: No-0, Yes-1')
    Senior_Citizen = st.number_input('Senior Citizen', 0, 1)

    st.write('Partner: No - 0, yes - 1')
    partner = st.number_input('Partner', 0,1)

    st.write('Dependents: No - 0, Yes - 1')
    Dependents = st.number_input('Dependents', 0, 1)

    st.write('Phone Service:Yes-0,No-1')
    PhoneService=st.number_input('Phone Service',0,1)

    st.write('Paperless Billing:Yes-0,No-1')
    PaperlessBilling=st.number_input('Paperless Billing',0,1)

    st.write('Multiple Lines:No-0,Yes-1,No Phone service-2')
    MultipleLines=st.number_input('MultipleLines',0,2)

    st.write('Internet Service:Fibre Optic-0, DSL-1,No-2')
    Internet_Service=st.number_input('Internet Service',0,2)

    st.write('Online Security:No-0,Yes-1, No Internet Service-2')
    Online_Security=st.number_input('Online Security',0,2)

    st.write('Online Backup:No-0,Yes-1, No Internet Service-2')
    Online_Backup=st.number_input('Online Backup',0,2)

    st.write('Device Protection :No-0,Yes-1, No Internet Service-2')
    Device_Protection=st.number_input('Device Protection',0,2)

    st.write(' Tech Support :No-0,Yes-1, No Internet Service-2')
    Tech_Support=st.number_input(' Tech Support',0,2)
    
    st.write(' StreamingTV :No-0,Yes-1, No Internet Service-2')
    StreamingTV=st.number_input(' StreamingTV',0,2)
    
    st.write(' Streaming Movies :No-0,Yes-1, No Internet Service-2')
    Streaming_Movies=st.number_input(' Streaming Movies',0,2)

    st.write(' Contract :Month-to-month-0, Two year-1,One year-2')
    Contract=st.number_input(' Contract',0,2)

    st.write('Payment Method: Electronic check-0,Mailed check-1,Bank Transfer(automatic)-2,Credit card(automatic)-3')
    Payment = st.number_input('Payment', 0, 3)

    st.write('Tenure: Numbers')
    tenure = st.number_input('Tenure',0, 72)


    st.write('Monthly Charges: Float or Numbers')
    Monthly_Charges = st.number_input('Monthly Charges', 0, 130)

    st.write('Total Charges: Float or Numbers')
    total_charges = st.number_input('Total Charges', 0, 8700)


    input = [[gender, partner, Dependents, PhoneService, PaperlessBilling, MultipleLines,
    Internet_Service, Online_Security, Online_Backup, Device_Protection, Tech_Support, StreamingTV, Streaming_Movies, Contract, Payment,Senior_Citizen, 
    tenure, Monthly_Charges, total_charges]]


    # Output
    
    
    potential="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;">Customers will Churn</h2>
       </div>
    """
    not_potential="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;">Customers will Not Churn</h2>
       </div>
    """

    if st.button('Predict'):
        output = model.predict(input)
        res  =  output.flatten().astype(float)

        if res > 0.5:
            st.markdown(potential, unsafe_allow_html = True)
            st.write('Suggestion: ')

        else:
            st.markdown(not_potential, unsafe_allow_html = True)
            st.write('Suggestion')


if __name__ == '__main__':
    main()