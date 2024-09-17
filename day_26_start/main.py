import pandas

# # with open("./weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# # with open("./weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #
# #     print(temperature)

# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # #print(data_dict)
# # temp_list = data["temp"].to_list()
# # sum = 0
# # for temp in temp_list:
# #     sum += temp
# # average_temp = sum / len(temp_list)
# # print(average_temp)
# # average_temp1 = data["temp"].mean()
# # max_temp = data["temp"].max()
# # print(average_temp1)
# # print(max_temp)
# # print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# to_fahrenheit = (monday_temp * 9/5) + 32
# print(to_fahrenheit)
# Creating Dataframe
# data_dict = {
#                 "Student": ["Andy", "Mark", "Jax"],
#                 "Score": [70, 50, 50]
#             }
# df = pandas.DataFrame(data_dict)
# df.to_csv("New_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
value_count = data["Primary Fur Color"].value_counts()  # value_count() return the count of the different element in the
# column
data_list = value_count.to_list()
colour_list = ["Gray", "Cinnamon", "Black"]
data_dict = {
    "Fur Colour": colour_list,
    "Count": data_list
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Fur_colour_count.csv")
