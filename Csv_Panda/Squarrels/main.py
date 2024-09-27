
import pandas
data = pandas.read_csv("Csv_Panda/Squarrels/data.csv")

data_gray = len(data[data["Primary Fur Color"] == "Gray"])
data_black = len(data[data["Primary Fur Color"] == "Black"])
data_cinammon = len(data[data["Primary Fur Color"] == "Cinnamon"])

# print(f"There are, {data_gray} Gray Squarells")
# print(f"There are, {data_black} Black Squarells")
# print(f"There are, {data_cinammon} Cinnamon Squarells")

data_frame = {
    "Gray Squarrells" : data_gray,
    "Black Squarells" : data_black,
    "Cinnamon Squarells" : data_cinammon
}

newData = pandas.DataFrame(data_frame)
newData.to_csv("exact_data.csv")