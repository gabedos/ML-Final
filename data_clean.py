import pandas as pd


if __name__ == '__main__':

    df = pd.read_csv('Recidivism.csv')

    # print(df.head())

    # GENDER: Male -> True, Female -> False
    df['Gender'] = df['Gender'].map({'M': True, 'F': False})

    # RACE: White -> True, Black -> False
    df['Race'] = df['Race'].map({"WHITE": True, "BLACK": False})

    # AGE AT RELEASE: One hot encoding
    dummies = pd.get_dummies(df['Age_at_Release'], prefix='age')
    df = pd.concat([df, dummies], axis=1)
    df.rename(columns={'age_48 or older': 'age_48+'},inplace=True)
    df.drop('Age_at_Release', axis=1, inplace=True)

    # EDUCATION LEVEL: One hot encoding
    dummies = pd.get_dummies(df['Education_Level'], prefix='educ')
    df = pd.concat([df, dummies], axis=1)
    df.rename(columns={
        'educ_At least some college': 'educ_high_school_plus',
        'educ_High School Diploma': 'educ_high_school',
        'educ_Less than HS diploma': 'educ_high_school_minus',
        },
        inplace=True)
    df.drop('Education_Level', axis=1, inplace=True)

    # DEPENDENTS: One hot encoding
    dummies = pd.get_dummies(df['Dependents'], prefix='dependents')
    df = pd.concat([df, dummies], axis=1)
    df.rename(columns={'dependents_3 or more': 'dependents_3+'}, inplace=True)
    df.drop('Dependents', axis=1, inplace=True)



    # df['Gang_Affiliated'] = df['Gang_Affiliated'].map({True: True, False: False})
    # print(df['Gang_Affiliated'].unique())

    # Print the types of all the columns in the dataframe
    print(df.dtypes[:20])
    print()
    print(df.dtypes[50:])

