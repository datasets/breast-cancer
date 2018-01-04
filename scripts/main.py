from urllib.request import urlopen

with open("../data/breast-cancer.csv", "w") as bumps_file:
    # bumps_file.write("season,age,childish-disease,trauma,surgical-intervention,fevers,alcoholic,"
    #                  "smoking,sitting,output\n")
    for line in urlopen("https://www.openml.org/data/get_csv/13/dataset_13_breast-cancer.arff"):
        decodedLine = line.decode('UTF-8')
        decodedLine = decodedLine.replace('?', '')
        decodedLine = decodedLine.replace('"', '')
        decodedLine = decodedLine.replace('\'', '')
        decodedLine = decodedLine.replace('yes', 'true')
        decodedLine = decodedLine.replace('no', 'false')
        decodedLine = decodedLine.lower()
        print(decodedLine.strip())
        bumps_file.write(decodedLine.strip() + '\n')
    bumps_file.close()
