import os, glob
import pandas as pd
import csv

if name == 'main':
  path = ""

  all_files = glob.glob(os.path.join(path, "LTE*.csv"))
  df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
  df_merged   = pd.concat(df_from_each_file, ignore_index=True)
  df_merged.to_csv("merged.csv")


def combine_csv(input_filename , output_filename, path, **kwargs):
  
  all_files = glob.glob(os.path.join(path, input_filename))
  df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
  df_merged   = pd.concat(df_from_each_file, ignore_index=True)
  df_merged.to_csv(output_filename)
  return df_merged


def delete_csv(filename):
  my_dir = "."
  for fname in os.listdir(my_dir):
    if fname.startswith(filename):
      os.remove(os.path.join(my_dir, fname))


def csv_to_list(filename):
  inputm = []
  with open(filename, "rt") as f:
    reader = csv.reader(f, dialect='excel',delimiter=",")
    for row in reader:
      entry = row[0]
      entry = ''.join([x for x in entry if x in string.printable]).replace(' ','_').replace('\n','').replace('\r','')
      inputm.append(str(entry))
  print(f"""read from csv file..  = {inputm}""")
  return inputm


def csv_to_dict(filename):
  mydict = {}

  with open(filename, mode='r') as inp:
      reader = csv.reader(inp)
      dict_from_csv = {rows[0]:rows[1] for rows in reader}

  print(dict_from_csv)
  return dict_from_csv