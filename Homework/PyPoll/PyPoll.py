import os
import csv

csvpath = os.path.join('/Users', 'neimical', 'Desktop', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    election = csv.reader(csvfile, delimiter=',')
    print(election)

    Khan = []
    Correy = []
    Li = []
    Tooley = []
    Total = []

    csv_header = next(election)
    print(f"Elections results")
    print("-------------------")

    print(csv_header)

    total_votes = 0
    net_Khan = 0
    average_Khan = 0
    net_Correy = 0
    average_Correy = 0
    net_Li = 0
    average_Li = 0
    net_Tooley = 0
    average_Tooley = 0

 #Read each row of data after the header
    for row in election:
        total_votes += 1
        if row[2] == 'Khan':
            net_Khan = int(row[0])
            Khan.append(net_Khan)
        elif row[2] == 'Correy':
            net_Correy = int(row[0])
            Correy.append(net_Correy)
        elif row[2] == 'Li':
            net_Li = int(row[0])
            Li.append(net_Li)
        elif row[2] == "O'Tooley":
            net_Tooley = int(row[0])
            Tooley.append(net_Tooley)


    percentage_Khan = len(Khan) / total_votes * 100
    percentage_Correy = len(Correy) / total_votes * 100
    percentage_Li = len(Li) / total_votes * 100
    percentage_Tooley = len(Tooley) / total_votes * 100

    print(f"Total Votes: {total_votes}")
    print(f"Khan: {round(percentage_Khan), 2} % {len(Khan)}")
    print(f"Total: {round(percentage_Correy), 2} % {len(Correy)}")
    print(f"Total: {round(percentage_Li), 2} % {len(Li)}")
    print(f"Total: {round(percentage_Tooley, 2)} % {len(Tooley)}")
    print("--------------------------------")
    print("Winer = Khan")
    print("--------------------------------")
