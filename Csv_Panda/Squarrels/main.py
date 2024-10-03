
import pandas
data = pandas.read_csv("Csv_Panda/Squarrels/data.csv")

data_gray = len(data[data["Primary Fur Color"] == "Gray"])
data_black = len(data[data["Primary Fur Color"] == "Black"])
data_cinammon = len(data[data["Primary Fur Color"] == "Cinnamon"])


# Dictionary containing the counts for each fur color
# data_frame = {
#     "Gray Squarrells": data_gray,
#     "Black Squarells": data_black,
#     "Cinnamon Squarells": data_cinammon
# }
data_dict = {
    "Fur Color": ["Gray", "Cinammon", "Black"],
    "Count": [data_gray, data_cinammon, data_black]

} 

# Create a DataFrame and save it as a CSV file
newData = pandas.DataFrame(data_dict)  # Wrap data_frame in a list
newData.to_csv("exact_data.csv")  # Write DataFrame to CSV without row index