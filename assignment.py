# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def clean_degrees(df):
    df = (df.drop('Unnamed: 0', axis=1)
          .rename(columns={'Unnamed: 1': 'Country', 'Unnamed: 2': 'Degree'})
          .set_index(['Country'])
          )
    return df


def clean_religion(df):
    df = (df
          .rename(columns={'Bundesland': 'Country', 'Einwohner': 'Population', 'Katholisch': 'Catholic', 'Evangelisch': 'Protestant'})
          .set_index(['Country'])
          )
    return df


def merge_data(df1, df2):
    return pd.merge(df1, df2, how='inner', left_index=True, right_index=True)


def plot_catholic(ax):
    ax.bar(df['Population'].index, df['Catholic']/df['Population'] * 100)
    create_labels(ax)
    plot_degree(ax)
    ax.set_title('Catholics in german countries')

def plot_protestant(ax):
    ax.bar(df['Population'].index, df['Protestant']/df['Population'] * 100)
    create_labels(ax)
    plot_degree(ax)
    ax.set_title('Protestants in german countries')
    plt.legend(( 'Protestant'))

def plot_degree(ax):
    ax_degree = ax.twinx() 
    ax_degree.set_ylabel('Ø degree of graduates', color='yellow')
    ax_degree.plot(df['Degree'], color='yellow')

def create_labels(ax):
    ax.set_xlabel('Country')
    ax.set_ylabel('Pop. in %')
    plt.xticks(rotation='vertical')

def plot_data():
    f, (ax1, ax2) = plt.subplots(2, 1, sharey=True, sharex=True)
    plt.subplots_adjust(hspace=0.5)
    plot_catholic(ax1)
    plot_protestant(ax2)

religion_per_country = pd.read_excel('ReligionperCountry.xlsx', skiprows=1)
degrees_per_country = pd.read_excel(
    'statistic_id36277_durchschnittliche-abiturnoten-in-deutschland-nach-bundeslaendern-2017.xlsx', sheet_name=1, skiprows=4)

degrees_per_country = clean_degrees(degrees_per_country)
religion_per_country = clean_religion(religion_per_country)
df = merge_data(degrees_per_country, religion_per_country)

plot_data()


ttest_protestant_degree = stats.ttest_ind( df['Protestant'],  df['Degree'])
ttest_catholic_degree = stats.ttest_ind( df['Catholic'],  df['Degree'])

if ttest_protestant_degree.pvalue < 0.01:
    protestent_significant = True
else:
    protestent_significant = False
print('Significant (p < 0.01) correlation between percentage of protestant population per country and the average high school graduates degree?')
print(protestent_significant)
if ttest_catholic_degree.pvalue < 0.01:
    catholic_significant = True
else:
    catholic_significant = False
print('Significant (p < 0.01) correlation between percentage of catholic population per country and the average high school graduates degree?')
print(catholic_significant)

# %%
