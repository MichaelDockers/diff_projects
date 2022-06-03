import os
import pandas as pd

# Initialization block

file_filter_str = '2.14'
root_folder = 'E:\\PythonAmp\\2022-03-10 19_13_38'
output_filename = 'output_name'

df = pd.DataFrame()

# Function block

def get_folders_in_root_list(root_folder: str) -> list:
    '''Returns folders list in root folder except HistorySignal and Statistic'''

    return [x.path for x in os.scandir(root_folder) if x.is_dir() and ('HistorySignal' not in str(x) and 'Statistic' not in str(x))]


def get_maxnumbered_file(folder: str, file_filter_str: str) -> str:
    '''Getting file with max number in list filtered by specified string'''
    
    files_in_folder = [x.path.split('\\')[-1] for x in os.scandir(folder) if (x.is_file() and file_filter_str in str(x))]
    return max(files_in_folder, key=lambda x: int(x.split('$')[-1][:2]))


def get_df_for_folder(file_name: str, inst_name: str) -> pd.DataFrame:
    '''Returning DataFrame contains factor for current folder and selected file. Factor's name changed to inst / factor'''

    factor_df = pd.read_csv(file_name)
    factor_df['Date'] = pd.to_datetime(factor_df['Date'])
    factor_df.set_index('Date', inplace=True)
    col = factor_df.columns.to_list()[0]
    factor_df.rename(columns={col: f'{col} / {inst_name}'}, inplace=True)
    return factor_df


folders = get_folders_in_root_list(root_folder)
for folder in folders:
    inst_name = folder.split('\\')[-1]
    try:
        file_str = f'{folder}\\{get_maxnumbered_file(folder, file_filter_str)}'
        df = pd.concat([df, get_df_for_folder(file_str, inst_name)], axis=1)
    except ValueError:
        print(f'[-] No 2.14 files in directory {folder}')

df.to_csv(f'{root_folder}\\{output_filename}.csv')
