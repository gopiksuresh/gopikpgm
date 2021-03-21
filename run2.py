
input_file = open('sample_input2.txt', 'r')
output_file = open('sample_output2.txt', 'w')

employees_count = int(input_file.readline().split(":")[1].strip())
input_file.readline() # Ignore next empty line
input_file.readline() # Ignore line with goodies
input_file.readline() # Ignore next empty line

items_list = []
for input_items in input_file.readlines():
    item_name = input_items.split(":")[0].strip()
    item_price = int(input_items.split(":")[1].strip())
    items_list.append((item_price, item_name))

items_list.sort()

end_index = employees_count - 1
max_difference = items_list[end_index][0] - items_list[0][0]
for i in range(employees_count, len(items_list)):
    if items_list[i][0] - items_list[i - (employees_count - 1)][0] < max_difference:
        max_difference = items_list[i][0] - items_list[i - (employees_count - 1)][0]
        end_index = i

print("The goodies selected for distribution are:\n", file=output_file)
for i in range(end_index - employees_count + 1, end_index + 1):
        print(items_list[i][1],": ",items_list[i][0], file=output_file)

print("\nAnd the difference between the chosen goodie with highest price and the lowest price is ",max_difference, file=output_file)

input_file.close()
output_file.close()
