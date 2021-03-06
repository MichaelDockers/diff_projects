import os
from textwrap import indent
from tkinter import image_names
from matplotlib import dates
import pandas as pd
import numpy as np

# Initialization block

factor_filter_str = '2.14'
amp_filter_str = '1.08'
inst_filter_str = '2.13'
target_value = 0.3

root_folder = 'E:\\PythonAmp\\2022-03-10 19_13_38'
history_signal_folder = f'{root_folder}\\HistorySignal'
output_filename = 'output_name'

df = pd.DataFrame(index=pd.to_datetime([]))


def get_folders_in_history_signal(folder: str) -> list:
    '''Returns folders list in root folder except HistorySignal and Statistic'''

    return [x.path for x in os.scandir(folder) if x.is_dir()]


def get_maxnumbered_history_file(folder: str) -> str:
    '''Getting file with max number in folder'''

    files_in_folder = [x.path.split('\\')[-1] for x in os.scandir(folder) if x.is_file()]
    return max(files_in_folder, key=lambda x: int(x.split('.')[0]))


def get_maxnumbered_file(folder: str, file_filter_str: str) -> str:
    '''Getting file with max number in list filtered by specified string'''
    
    files_in_folder = [x.path.split('\\')[-1] for x in os.scandir(folder) if (x.is_file() and file_filter_str in str(x))]
    return max(files_in_folder, key=lambda x: int(x.split('$')[-1][:2]))


def get_result_df(hist_str: str, amp_str: str, instr_str: str, instrument_name: str) -> pd.DataFrame:
    '''
    Result - DataFrame for Instrument
    hist_str - file with path to History Signal
    amp_str - file with path to Amplitude
    instr_str - file with path to Instrument Returns
    instrument_name - instrument name by folder name (to name column in df)
    result = sum(all hist columns / amplit (not align by date) * Instrument Returns (by pair and align by date))
    '''

    df_hist = pd.read_csv(hist_str)
    df_amplit = pd.read_csv(amp_str)
    df_instr = pd.read_csv(instr_str)

    df_hist_div_amp = pd.concat([df_hist['Date'], df_hist.drop('Date', axis=1).div(np.sqrt(df_amplit.drop('Date', axis=1).iloc[:, 0]), axis=0)], axis=1)

    df_hist_div_amp.dropna(how='all', inplace=True)
    df_hist_div_amp['Date'] = pd.to_datetime(df_hist_div_amp['Date'])
    df_hist_div_amp.set_index('Date', inplace=True)

    df_instr['Date'] = pd.to_datetime(df_instr['Date'])
    df_instr.set_index('Date', inplace=True)

    first_hist_idx = df_hist_div_amp.index.min()
    last_hist_idx = df_hist_div_amp.index.max()

    first_instr_idx = df_instr.index.min()
    last_instr_idx = df_instr.index.max()

    min_date = max(first_hist_idx, first_instr_idx)
    max_date = min(last_hist_idx, last_instr_idx)

    if pd.infer_freq(df_hist_div_amp.index) != 'B':
        print(f'[-] {instrument_name} is not dayly. Filling forward...')
        df_hist_div_amp.asfreq('B')
        if last_hist_idx < last_instr_idx:
            print(f'[-] {instrument_name} history signal ending before Instrument Returns. Adding last return"s date and filing NaNs')
            print(f'Before: Max hist: {last_hist_idx}, Max inst {last_instr_idx}')
            df_hist_div_amp.loc[pd.to_datetime(last_instr_idx)] = pd.Series(dtype='float64')
            print(f'After: Max hist: {df_hist_div_amp.index.max()}, Max inst {last_instr_idx}')
       
        df_hist_div_amp = df_hist_div_amp.resample('B').asfreq().ffill()
        
        print(f'Instrument: {instrument_name}')
        print(f'Min/Max date of history signal by sqrt of amplitude: {first_hist_idx.date()}, {last_hist_idx.date()}')
        print(f'Min/Max date of return: {first_instr_idx.date()}, {last_instr_idx.date()}')
        print(f'Begin and end of cut period: {min_date.date()}, {df_hist_div_amp.index.max()}')

        return df_hist_div_amp.loc[min_date: df_instr.index.max()].mul(df_instr.loc[min_date: df_instr.index.max()]).sum(axis=1)

    print(f'Instrument: {instrument_name}')
    print(f'Min/Max date of history signal by sqrt of amplitude: {first_hist_idx.date()}, {last_hist_idx.date()}')
    print(f'Min/Max date of return: {first_instr_idx.date()}, {last_instr_idx.date()}')
    print(f'Begin and end of cut period: {min_date.date()}, {max_date.date()}')

    return df_hist_div_amp.loc[min_date: max_date].mul(df_instr.loc[min_date: max_date]).sum(axis=1)


folders = get_folders_in_history_signal(history_signal_folder)
    
for folder in folders:
    instrument_name = folder.split('\\')[-1]
    history_file = f'{folder}\\{get_maxnumbered_history_file(folder)}'
    root_instrument_path = f'{root_folder}\\{instrument_name}'
    if os.path.exists(root_instrument_path):
        print(f'[+] folder {root_instrument_path} exists')
        try:
            amplitude_file = f'{root_instrument_path}\\{get_maxnumbered_file(root_instrument_path, amp_filter_str)}'
            instrument_file = f'{root_instrument_path}\\{get_maxnumbered_file(root_instrument_path, inst_filter_str)}'
            df = pd.concat([df, get_result_df(history_file, amplitude_file, instrument_file, instrument_name).rename(instrument_name)], axis=1)
        except ValueError:
            print(f'[-] No 1.08 or 2.13 files in directory {root_instrument_path}')
    else:
        print(f'[-] No {folder} in root directory')

df.to_csv(f'{root_folder}\\df_result_result.csv', index_label='Date')

for col in df._get_numeric_data():
    df[col] = df[col] * (target_value / np.std(df[col]))

df.to_csv(f'{root_folder}\\df_result_vol.csv', index_label='Date')