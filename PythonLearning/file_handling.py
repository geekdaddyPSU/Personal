"""
file_path = "example.txt"
try:
	with open(file_path, "r") as file:
		content = file.read()
		print("File content: ")
		print(content)
except FileNotFoundError:
	print(f"File: '{file_path}' not found")
"""

output_path = "output.txt"
data_to_write = "This is the output line\n"
try:
	with open(output_path, "w") as file:
		file.write(data_to_write)
	print(f"Data written to '{output_path}'")
except Exception as e:
	print("An exception occurred: ", e)
