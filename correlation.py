# Add the functions in this file
import json
import math
def load_journal(file1):
  with open(file1) as j:
    data = json.load(j)
    return data  

def compute_phi(file1, event):
  data_dict = load_journal(file1)
  both_true=0
  both_false=0
  x_true=0
  y_true=0
  for i in range(len(data_dict)):
    if event in data_dict[i]["events"] and data_dict[i]["squirrel"]:
      both_true+=1
    elif event in data_dict[i]["events"]:
      x_true+=1
    elif data_dict[i]["squirrel"]:
      y_true+=1
    else:
      both_false+=1  


  only_x = both_true + x_true
  only_y = both_true + y_true
  not_x = both_false + y_true
  not_y = both_false + x_true    
  corr = (both_true*both_false - x_true*y_true)/math.sqrt(only_x*only_y*not_x*not_y)

  return corr

def compute_correlations(file1):
  journal_file = load_journal(file1)
  events ={}
  event_lol=[]
  for i in range(len(journal_file)):
    event_x = journal_file[i]["events"]
    for j in event_x:
      if j not in event_lol:
        event_lol.append(j)
  for k in event_lol:
    events[k] = compute_phi(journal_file, k)

  return events

def diagnose(file1):
  journal_file = load_journal(file)
  events = compute_correlations(journal_file)
  max_key = max(events, key=events.get)
  min_key = min(events, key=events.get)
  
  return (max_key, min_key)
