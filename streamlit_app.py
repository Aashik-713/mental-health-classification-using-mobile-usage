import streamlit as st
import pickle

with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

age_options = {'16-20': 0, '21-25': 1}
gender_options = {'Male': 1, 'Female': 0}
os_options = {'Android': 1, 'IOS': 0}
edu_use_options = {'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Frequently': 3}
activities_options = {'Messaging': 0, 'Web-browsing': 1, 'Social Media': 2, 'All of these': 3}
helpful_options = {'Yes': 1, 'No': 0}
edu_apps_options = {'Productivity Tools': 0, 'Language': 1, 'Study Planner': 2, 'Educational Videos': 3}
daily_usage_options = {'< 2 hours': 0, '2-4 hours': 2, '4-6 hours': 3, '> 6 hours': 1}
performance_impact_options = {'Disagree': 0, 'Neutral': 1, 'Agree': 2, 'Strongly disagree': 3, 'Strongly agree': 4}
usage_distraction_options = {'Not Distracting': 1, 'While Studying': 2, 'During Class Lectures': 3, 'During Exams': 0}
attention_span_options = {'Yes': 1, 'No': 0}
useful_features_options = {'Calculator': 0, 'Notes Taking App': 1, 'Camera': 2, 'Internet Access': 3}
health_risks_options = {'No': 0, 'Only Partially': 1, 'Yes': 2}
beneficial_subject_options = {'Accounting': 0, 'Browsing Material': 1, 'Reasarch': 2}
usage_symptoms_options = {'Anxiety or Stress': 0, 'Sleep disturbance': 1, 'Headache': 2, 'All of these': 3}
symptom_frequency_options = {'Never': 1, 'Rarely': 2, 'Sometimes': 3, 'Frequently': 0}
health_precautions_options = {'Using Blue light filter': 0, 'Taking Break during prolonged use': 1, 'None of Above': 2, 'Limiting Screen Time': 3}

def get_features():
    features = [
        age_options.get(age),
        gender_options.get(gender),
        os_options.get(mobile_os),
        edu_use_options.get(edu_use),
        activities_options.get(mobile_activities),
        helpful_options.get(helpful_studying),
        edu_apps_options.get(edu_apps),
        daily_usage_options.get(daily_usages),
        performance_impact_options.get(performance_impact),
        usage_distraction_options.get(usage_distraction),
        attention_span_options.get(attention_span),
        useful_features_options.get(useful_features),
        health_risks_options.get(health_risks),
        beneficial_subject_options.get(beneficial_subject),
        usage_symptoms_options.get(usage_symptoms),
        symptom_frequency_options.get(symptom_frequency),
        health_precautions_options.get(health_precautions)
    ]
    return features

st.title('Mobile Phone Usage Survey')
st.header('Fill In The Details')

with st.container():
    col1, col2, col3 = st.columns([2, 2, 2])

    with col1:
        age = st.selectbox('Age', options=[None] + list(age_options.keys()), format_func=lambda x: x if x else "Select Age")
        gender = st.selectbox('Gender', options=[None] + list(gender_options.keys()), format_func=lambda x: x if x else "Select Gender")
        mobile_os = st.selectbox('Mobile Operating System', options=[None] + list(os_options.keys()), format_func=lambda x: x if x else "Select OS")
        edu_use = st.selectbox('Mobile phone use for education', options=[None] + list(edu_use_options.keys()), format_func=lambda x: x if x else "Select Education Use")
        performance_impact = st.selectbox('Performance impact', options=[None] + list(performance_impact_options.keys()), format_func=lambda x: x if x else "Select Impact")
        
    
    with col2:
        mobile_activities = st.selectbox('Mobile phone activities', options=[None] + list(activities_options.keys()), format_func=lambda x: x if x else "Select Activities")
        helpful_studying = st.selectbox('Helpful for studying', options=[None] + list(helpful_options.keys()), format_func=lambda x: x if x else "Select Studying Help")
        edu_apps = st.selectbox('Educational Apps', options=[None] + list(edu_apps_options.keys()), format_func=lambda x: x if x else "Select Educational Apps")
        attention_span = st.selectbox('Attention span', options=[None] + list(attention_span_options.keys()), format_func=lambda x: x if x else "Select Attention Span")
        symptom_frequency = st.selectbox('Symptom frequency', options=[None] + list(symptom_frequency_options.keys()), format_func=lambda x: x if x else "Select Symptom Frequency")

    with col3:
        useful_features = st.selectbox('Useful features', options=[None] + list(useful_features_options.keys()), format_func=lambda x: x if x else "Select Useful Features")
        health_risks = st.selectbox('Health Risks', options=[None] + list(health_risks_options.keys()), format_func=lambda x: x if x else "Select Health Risks")
        beneficial_subject = st.selectbox('Beneficial subject', options=[None] + list(beneficial_subject_options.keys()), format_func=lambda x: x if x else "Select Beneficial Subject")
        usage_symptoms = st.selectbox('Usage symptoms', options=[None] + list(usage_symptoms_options.keys()), format_func=lambda x: x if x else "Select Symptoms")
        usage_distraction = st.selectbox('Usage distraction', options=[None] + list(usage_distraction_options.keys()), format_func=lambda x: x if x else "Select Distraction")

health_precautions = st.selectbox('Health precautions', options=[None] + list(health_precautions_options.keys()), format_func=lambda x: x if x else "Select Health Precautions")
daily_usages = st.selectbox('Daily usages', options=[None] + list(daily_usage_options.keys()), format_func=lambda x: x if x else "Select Daily Usage")

st.write("\n\n")
if st.button('Submit'):
    features = get_features()
    
    if None in features:
        st.error("Please select all options before submitting.")
    else:
        prediction = model.predict([features])
        
        if prediction == 0:
            st.markdown(
                "<h1 style='color: red;'>The mental health should be improved 😔</h1>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<h1 style='color: green;'>Congratulations, you're doing good! 😊</h1>",
                unsafe_allow_html=True
            )
