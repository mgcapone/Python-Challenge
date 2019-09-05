import os
import csv

ElectionCSV = os.path.join('..','PyPoll','election_data.csv')


with open(ElectionCSV,'r') as function:
    reader = csv.reader(function,delimiter=',')
    next(reader)
    candidates = []
    for row in csv.reader(function):
        if row[2] not in candidates:
            candidates.append(row[2])

with open(ElectionCSV,'r') as function:
    reader = csv.reader(function,delimiter=',')
    next(reader)
    Data = []
    for row in csv.reader(function):
        Data = row[2]
        KhanVotes = Data.count('Khan')
        #TotalKhanVotes = sum(KhanVotes)
        print(Data)
