import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?

    # A mask for men.
    men = df['sex'] == 'Male'

    average_age_men = round(df[men]['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    n_bachelors = df[df['education']=='Bachelors']['education'].size
    total_ed = df['education'].size
    percentage_bachelors = round(n_bachelors/total_ed*100, 1)

    # What percentage of people with advanced education
    # (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # A mask for higher-ed 
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    # A mask for, well, non-higer-ed.
    lower_education = ~higher_education

    n_high_ed = df[higher_education].size
    n_low_ed = df[lower_education].size

    n_high_rich = df[higher_education & (df['salary'] == '>50K')].size
    n_low_rich = df[lower_education & (df['salary'] == '>50K')].size
    
    higher_education_rich = round((n_high_rich/n_high_ed)*100, 1)
    lower_education_rich = round((n_low_rich/n_low_ed)*100, 1)

    # What is the minimum number of hours a person works per week
    # (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours
    # per week have a salary of >50K?
    
    # Mask for lazy people.
    lazy = df['hours-per-week']==1

    num_lazy = df[lazy].size
    num_lazy_rich = df[lazy & (df['salary'] == '>50K')].size
    
    rich_percentage = round((num_lazy_rich/num_lazy)*100, 1)

    # What country has the highest percentage of people that earn >50K?

    # A mask for the rich.
    rich = df['salary'] == '>50K'
    # Gives how many rich people by country.
    rich_countries = df[rich]['native-country'].value_counts()
    # How many people, in general, by country.
    countries = df['native-country'].value_counts()

    # What is the highest percentage of high earners?
    highest_earning_country_ = max(rich_countries/countries)

    # Who has that percentage?
    highest_earning_country = (rich_countries[(rich_countries/countries) == 
    							highest_earning_country_].index[0])
    # Rounding stuff.
    highest_earning_country_percentage = round(highest_earning_country_*100, 1)
    

    # Identify the most popular occupation for those who earn >50K in India.

    # A mask for Indians.
    indian = df['native-country'] == 'India'
    # Both indian and rich
    rich_indians = df[rich & indian]
    # Same logic used in highest_earning_country. Look it up in line 60.
    top_IN_occupation = rich_indians['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }