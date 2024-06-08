"""
Fast project to practice the use of the Python language, and learn how to use the NumPy library and Pandas library.

# Project Description
The project is a simple project that uses the NumPy library and the Pandas library to analyze a dataset. 
The dataset contains information about the Tree Species in Metropolitan France. 

More about the dataset, please visit the link below:
https://inventaire-forestier.ign.fr/dataifn/DonneesBrutes/afficherDonnees

or read the IGN_DB_doc_placette file in the dataset project folder. It is in french, sorry.

"""


# Importing the necessary libraries
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


directory = os.path.dirname(__file__)


def explore_dataset(dataset):
    # Display the first 5 rows of the dataset
    print(dataset.head())
    print('\n\n')

    # Display the last 5 rows of the dataset
    print(dataset.tail())
    print('\n\n')

    # Display the shape of the dataset
    print(dataset.shape)
    print('\n\n')

    # Display the columns of the dataset
    print(dataset.columns)
    print('\n\n')

    # Display the information about the dataset
    print(dataset.info())
    print('\n\n')

    # Display the description of the dataset
    print(dataset.describe())
    print('\n\n')

    # Display the number of missing values in the dataset
    print(dataset.isnull().sum())
    print('\n\n')

    # Display the number of unique values in the dataset
    print(dataset.nunique())
    print('\n\n')

def cleaning_dataset(dataset):
    # remove unnamed columns
    dataset.drop(dataset.columns[dataset.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    # rename the columns
    dataset.rename(columns={
        'CAMPAGNE': 'year_of_inventory', # CAMPAGNE: Annual inventory campaign (field operations); Year of field operations for an annual national forest inventory campaign;
        'IDP': 'plot_identifier', # IDP: External plot identifier; Identifier used when exporting plot data outside of IGN;
        'XL': 'longitude', # XL: Longitude Lambert 93; Geographic coordinate of the plot center;
        'YL': 'latitude', # YL: Latitude Lambert 93; Geographic coordinate of the plot center;
        'DEP': 'department_number', # DEP: Department; Administrative department number (similar to a license plate number);
        'Libellé DEP': 'derpartment_name',
        'TPESPAR1': 'species_code', # TPESPAR1: Main planted species; Species planted in a monospecific plantation, or the majority species planted in a mixed plantation.
        'Libellé TPESPAR1': 'species_name'
    }, inplace=True)
    

    return dataset

def species_by_department(dataset):
    df = dataset.copy()

    # Grouping department names by species name
    grouped_df = df.groupby('derpartment_name')['species_name'].apply(list).reset_index()

    # Rename columns for clarity
    grouped_df.columns = ['derpartment_name', 'species_name']

    # Display the grouped data
    print(grouped_df)

def species_by_department_count(dataset):
    df = dataset.copy()

    # Grouping department names by species name
    grouped_df = df.groupby('derpartment_name')['species_name'].apply(lambda x: np.unique(x).size).reset_index()

    # Rename columns for clarity
    grouped_df.columns = ['derpartment', 'unique_species_count']

    # Display the grouped data
    print(grouped_df)
    return grouped_df

def plot_species_by_department_count(dataset):
    df = dataset.copy()

    # Grouping by department name and counting unique species using numpy
    grouped_df = species_by_department_count(df)

    # Sorting by UniqueSpeciesCount in ascending order
    grouped_df = grouped_df.sort_values(by='unique_species_count', ascending=True)
    data = grouped_df.tail(30).copy()
    # Plotting
    plt.figure(figsize=(15, 10))
    plt.barh(data['derpartment'], data['unique_species_count'], color='blue')
    plt.xlabel('Unique Species Count')
    plt.ylabel('Department')
    plt.title('Unique Species Count by Department')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Display the plot
    plt.show()

def main():
    # Importing the dataset to be used in the project
    # we use the pandas library to read the dataset
    dataset = pd.read_csv(f'{directory}/dataset/PLACETTE.csv', sep=';')

    # explore the dataset
    explore_dataset(dataset)

    # Cleaning the dataset, renaming the columns, and dropping the unnecessary columns
    dataset = cleaning_dataset(dataset)

    # recheck the dataset
    explore_dataset(dataset)

    # Group species by department
    species_by_department(dataset)

    # Group species by department and count the number of unique species
    species_by_department_count(dataset)

    # Plot the number of unique species by department
    plot_species_by_department_count(dataset)




if __name__ == '__main__':
    main()
    

    

    # # Display the number of unique values in the dataset
    # print(dataset.nunique())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['ESPECE'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['GENRE'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['FAMILLE'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEVEGETAL'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEFEUILLE'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEFRUIT'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEFLEUR'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEBOUTON'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEEPI'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEINFLO'].value_counts())
    # print('\n\n')

    # # Display the number of unique values in the dataset
    # print(dataset['TYPEFRUCTIF'].value_counts())
    # print('\n\n')