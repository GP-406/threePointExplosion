import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_csv_data(file_path):
    dataFile = pd.read_csv(file_path)

    # converts the season column from float to string
    # sorts the season column in ascending order
    dataFile['Season'] = dataFile['Season'].astype(str)
    dataFile = dataFile.sort_values(by='Season')

    # Use the correct column names from your CSV file
    season = dataFile['Season']
    fg = dataFile['FG']
    fga = dataFile['FGA']
    three_pointers = dataFile['3P']
    three_pointers_attempted = dataFile['3PA']
    ft = dataFile['FT']
    fta = dataFile['FTA']
    orb = dataFile['ORB']
    drb = dataFile['DRB']
    trb = dataFile['TRB']
    ast = dataFile['AST']
    stl = dataFile['STL']
    blk = dataFile['BLK']

    # Plot various columns against 'Season'
    plt.plot(season, fg, label='FG')
    plt.plot(season, fga, label='FGA')
    plt.plot(season, three_pointers, label='3P')
    plt.plot(season, three_pointers_attempted, label='3PA')
    #plt.plot(season, ft, label='FT')
    #plt.plot(season, fta, label='FTA')
   # plt.plot(season, orb, label='ORB')
    #plt.plot(season, drb, label='DRB')
    plt.plot(season, trb, label='TRB')
    plt.plot(season, ast, label='AST')
    plt.plot(season, stl, label='STL')
    plt.plot(season, blk, label='BLK')

    
    index_1979 = season.where(season == '1979').first_valid_index()

    # Add a vertical line at the position of the label '1979'
    if index_1979 is not None:
        plt.axvline(x=index_1979, color='red', linestyle='--', label='Vertical Line at 1979')


    #plt.xlabel('Season')
    plt.ylabel('Values')
    plt.title('CSV Data Visualization')

    # Add more scatter plots as needed

    plt.xlabel('Years')
    plt.ylabel('Stats')
    plt.title('Three Point Explosion')

    plt.xticks(rotation=90, ha="right", fontsize = 5)
    plt.xticks(range(len(season)), [year.split('-')[0] for year in season])

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

# Get the absolute path to the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file
csv_file_path = os.path.join(current_directory, '3pe.csv')  # Replace 'your_file.csv' with your actual file name

# Plot the data
plot_csv_data(csv_file_path)
