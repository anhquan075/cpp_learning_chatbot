import os 
import json 
import argparse
from tabulate import tabulate
import pandas as pd
import dataframe_image as dfi


def get_data_errors(json_file, options=0):
    with open(json_file, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    if json_file.split('/')[-1].split('.')[0].split('_')[0] == 'intent':
        for data in datas:
            print(data['text'] + '\t||\t' + data['intent'] + '\t||\t' + data['intent_prediction']['name'])
    elif json_file.split('/')[-1].split('.')[0].split('_')[0] == 'DIETClassifier':
        for data in datas:
            if options == 1:
                if not data['predicted_entities']:
                    print(data['text'])
            elif options == 2:
                if not data['entities']:
                    print(data['text'])
            elif options == 3:
                if not data['entities'] and not data['predicted_entities']:
                    print(data['text'])
            else:
                raise ValueError("Options are 1, 2, 3. Please choose again")

def get_data_results():
    pass

def create_table(json_file, save_options=0):
    with open(json_file, 'r') as f:
        datas = json.load(f)
        
    dataframe = pd.DataFrame.from_dict(datas, orient='index').drop(columns=['confused_with'])
    if save_options == 1:
        dfi.export(dataframe,"mytable.png")
    elif save_options == 0:
        pass
    else:
        raise TypeError('Save options is only avaiable with 0: not save figure and 1: save figure')

    return tabulate(dataframe, headers='keys', tablefmt="fancy_grid")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Directory of json file", type=str)
    parser.add_argument("-o", "--options", help="Options to choose type to display data",type=int)
    parser.add_argument("-s", "--save", help="Save figure of results, default", type=int)
    args = parser.parse_args()

    # get_data_errors(args.data, args.options)
    table = create_table(args.data, args.save)
    print(table)