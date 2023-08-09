# Read the content from the text file
with open(r'C:\Users\GGPC\PycharmProjects\pythonProject\pyTorchLearning\dataset_balancer\task_mapping.txt', 'r') as file:
    content = file.readlines()

# Initialize an empty dictionary
result_dict = {}

# Process each line and populate the dictionary
for line in content:
    line = line.strip()  # Remove leading/trailing whitespace and newline characters
    parts = line.split()  # Split the line into parts using space as a separator
    if len(parts) == 2:
        key = parts[1]  # The second part is the key
        value = parts[0]  # The first part is the value
        result_dict[key] = value

print(result_dict)