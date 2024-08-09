
def preprocessing(df):
    df = df.drop(["Names","Mobile Phone"], axis=1)
    
    # Define consolidation functions
    def consolidate_activities(activity):
        if pd.isna(activity):
            return 'All of these' 
        if 'Social Media' in activity:
            return 'Social Media'
        elif 'Web-browsing' in activity:
            return 'Web-browsing'
        elif 'Messaging' in activity:
            return 'Messaging' 
        else:
            return 'All of these'
    
    def consolidate_health_rating(rating):
        if pd.isna(rating):
            return 'Good' 
        if 'Excellent;Good' in rating or 'Good' in rating:
            return 'Good'
        elif 'Excellent' in rating:
            return 'Excellent'
        elif 'Fair' in rating:
            return 'Fair'
        elif 'Poor' in rating:
            return 'Poor'
        else:
            return rating
    
    # Apply consolidation functions
    df['Mobile phone activities'] = df['Mobile phone activities'].apply(consolidate_activities)
    df['Health rating'] = df['Health rating'].apply(consolidate_health_rating)
    
    # Fill missing values with mode
    for column in df.columns:
        mode_value = df[column].mode()[0]  # Get the mode value
        df[column].fillna(mode_value, inplace=True)
    
    values_to_drop = ['26-30', '31-35']
    df=df[~df['Age'].isin(values_to_drop)]
    
    return df


def encoding(df):
    df['Age'] = df['Age'].map({'21-25': 1, '16-20': 0})
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df['Mobile Operating System'] = df['Mobile Operating System'].map({'Android': 1, 'IOS': 0})
    df['Mobile phone use for education'] = df['Mobile phone use for education'].map({'Sometimes': 3, 'Frequently': 2, 'Never': 0, 'Rarely': 1})
    df['Mobile phone activities'] = df['Mobile phone activities'].map({'All of these': 3, 'Social Media': 2, 'Web-browsing': 1, 'Messaging': 0})
    df['Helpful for studying'] = df['Helpful for studying'].map({'Yes': 1, 'No': 0})
    df['Educational Apps'] = df['Educational Apps'].map({'Educational Videos': 3, 'Study Planner': 2, 'Language': 1, 'Productivity Tools': 0})
    df['Daily usages'] = df['Daily usages'].map({'4-6 hours': 3, '2-4 hours': 2, '> 6 hours': 1, '< 2 hours': 0})
    df['Performance impact'] = df['Performance impact'].map({'Agree': 4, 'Neutral': 3, 'Strongly agree': 2, 'Strongly disagree': 1, 'Disagree': 0})
    df['Usage distraction'] = df['Usage distraction'].map({'While Studying': 3, 'During Class Lectures': 2, 'Not Distracting': 1, 'During Exams': 0})
    df['Attention span'] = df['Attention span'].map({'Yes': 1, 'No': 0})
    df['Useful features'] = df['Useful features'].map({'Internet Access': 3, 'Camera': 2, 'Notes Taking App': 1, 'Calculator': 0})
    df['Health Risks'] = df['Health Risks'].map({'Yes': 2, 'Only Partially': 1, 'No': 0})
    df['Beneficial subject'] = df['Beneficial subject'].map({'Reasarch': 2, 'Browsing Material': 1, 'Accounting': 0})
    df['Usage symptoms'] = df['Usage symptoms'].map({'All of these': 3, 'Headache': 2, 'Sleep disturbance': 1, 'Anxiety or Stress': 0})
    df['Symptom frequency'] = df['Symptom frequency'].map({'Sometimes': 3, 'Rarely': 2, 'Never': 1, 'Frequently': 0})
    df['Health precautions'] = df['Health precautions'].map({'Limiting Screen Time': 3, 'None of Above': 2, 'Taking Break during prolonged use': 1, 'Using Blue light filter': 0})
    df['Health rating'] = df['Health rating'].map({'Excellent': 1, 'Good': 0, 'Fair': 0, 'Poor': 0})
    for i in df.columns:
        df[i] = pd.to_numeric(df[i], errors='coerce').fillna(0).astype(int)
    return df
