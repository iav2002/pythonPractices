
# with open("/Users/ignacioalarconvarela/VsCode_Python/Csv_Panda/weather_data.csv") as data_file:
    # data = csv.reader(data_file)
    # temperatures = []
    # for row in data:
    #     if row[1] != "temp":
    #         temperatures.append(int(row[1]))
    # print(temperatures)

import pandas

# data = pandas.read_csv("/Users/ignacioalarconvarela/Developer/VsCode_Python/Csv_Panda/weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# #Se puede utilizar una serie al igual que una list en la cual podemos simplemente calcular distintas cosas usando metodos similares
# temp_list = data["temp"].to_list()

# # average =sum(temp_list) / len(temp_list)
# # print(average)

# print(data["temp"].mean())

# print(data["temp"].max())
# #print(max(temp_list))

# #pandas se encarga de visualizar todas tus tablas para poder usar las columnas de manera especifica 

# # print(data["condition"])
# print(data.condition)
 
data_dict = {
"students": ["Amy", "James", "Angela"],
"scores":[76,55,34]
}
data = pandas.DataFrame(data_dict)
data.to_csv("New_data.csv")