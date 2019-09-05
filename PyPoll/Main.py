import os
import csv

ElectionCSV = os.path.join('..','PyPoll','election_data.csv')
output_path = os.path.join('..','PyPoll','ElectionResults.txt',)

adict = dict()

with open(ElectionCSV,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    next(reader)
    for row in csv.reader(csvfile):
        adict[row[2]] = 0

with open(ElectionCSV,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    next(reader)
    for row in csv.reader(csvfile):
        adict[row[2]] += 1

TotalVotes = 0
for candidate in adict:
    TotalVotes += adict[candidate]

print('Election Results')
print('-----------------------------------------')
print('Total Votes: ' + str(TotalVotes))
print('-----------------------------------------')
for candidate in adict:

    print('{}: Votes ({}), Percent of Votes: {:.2%}'.format
    (candidate, adict[candidate], adict[candidate]/TotalVotes))
print('-----------------------------------------')
print('Winner: Khan!')

with open(output_path, 'w') as txt_file:
   textwriter = txt_file.write()