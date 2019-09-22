# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_degrees(df):
    df = (df.drop('Unnamed: 0', axis=1)
          .rename(columns={'Unnamed: 1': 'Country', 'Unnamed: 2': 'Degree'})
          .set_index(['Country'])
          )
    return df


def clean_religion(df):
    df = (df
          .rename(columns={'Bundesland': 'Country', 'Einwohner': 'Population', 'Katholisch': 'Catholic', 'Evangelisch': 'Evangelic'})
          .set_index(['Country'])
          )
    return df


def merge_data(df1, df2):
    return pd.merge(df1, df2, how='inner', left_index=True, right_index=True)


def plot_data():
    plt.bar(df['Population'].index, df['Population'])
    plt.bar(df['Population'].index, df['Catholic'])
    plt.bar(df['Population'].index, df['Evangelic'], bottom=df['Catholic'])

def create_labels():
    ax = plt.gca()
    ax.set_title('German countries: Relation of religion to their population')
    ax.set_xlabel('Country')
    ax.set_ylabel('Population in millions')
    plt.legend(('Other', 'Catholic', 'Evangelic'))
    plt.xticks(rotation='vertical')

religion_per_country = pd.read_excel('ReligionperCountry.xlsx', skiprows=1)
degrees_per_country = pd.read_excel(
    'statistic_id36277_durchschnittliche-abiturnoten-in-deutschland-nach-bundeslaendern-2017.xlsx', sheet_name=1, skiprows=4)

degrees_per_country = clean_degrees(degrees_per_country)
religion_per_country = clean_religion(religion_per_country)
df = merge_data(degrees_per_country, religion_per_country)


plot_data()
create_labels()

df


# %%
