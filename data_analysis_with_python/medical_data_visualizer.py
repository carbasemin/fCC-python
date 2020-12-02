import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# Calculating the BMI
bmi = df['weight'] / (df['height']/100)**2 
# Creating a new column that represents the BMI.
df["overweight"] = bmi
# If BMI is greater than 25, then the person is overweight, 1.
# If not, then the person is not overweight, 0.
df.loc[df["overweight"] <= 25, "overweight"] = 0
df.loc[df["overweight"] > 25, "overweight"] = 1

# Normalize data by making 0 always good and 1 always bad.
# If the value of 'cholestorol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1
df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df

    df_cat = pd.melt(df_cat, 'cardio',
    				['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )


    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable',
            col='cardio',
            hue='value',
            data=df_cat,
            kind='count')

    g.set_axis_labels("variable", "total")

    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    
	df_heat = df
   
    # Clean the data
	df_heat = df_heat[
	# Diastolic pressure (ap_lo) shouldn't be higher than 
    # systolic blood pressure (ap_hi).
	(df_heat["ap_lo"] <= df_heat["ap_hi"]) &
	# Getting rid of the outliers.
	(df_heat['height'] >= df_heat["height"].quantile(0.025)) &
	(df_heat['height'] <= df_heat["height"].quantile(0.975)) &
	(df_heat['weight'] >= df_heat["weight"].quantile(0.025)) &
	(df_heat['weight'] <= df_heat["weight"].quantile(0.975))
	]

    # Calculate the correlation matrix

	corr = df_heat.corr()

    # Generate a mask for the upper triangle
	mask = np.zeros_like(corr)
	mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    # Draw the heatmap with 'sns.heatmap()'
	with sns.axes_style("white"):
		fig, axis = plt.subplots(figsize=(15, 12))
		axis = sns.heatmap(corr, vmin=0.05, vmax=0.25, mask=mask, 
			fmt='.1f',
			annot=True,
        )


    # Do not modify the next two lines
	fig.savefig('heatmap.png')
	return fig