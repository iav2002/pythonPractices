import csv

with open("/Users/ignacioalarconvarela/VsCode_Python/Csv_Panda/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)