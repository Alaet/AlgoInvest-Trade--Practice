import csv


def read_files(files_names):
    actions = []
    for file_name in files_names:
        file = open(file_name)
        csvreader_file = csv.reader(file)
        for action in csvreader_file:
            if action[1] != "price":
                action[1] = (action[1])
                action[2] = (action[2])
                if float(action[1]) > 0 and float(action[2]) > 0:
                    actions.append(action)
    return actions


actions = read_files(["data/dataset1_Python.csv", "data/dataset2_Python.csv"])


def get_best_wallet(actions, capital):
    i = 0
    actions.sort(key=lambda x:x[2], reverse=True)
    best_wallet = []
    
print(actions)