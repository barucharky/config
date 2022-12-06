import os


test_dir = "/home/baruch/test"
dirname = "python_test_dir/pointless_dir/test_files"
file_name = "bh.txt"

print(os.getcwd())
os.chdir(test_dir)
print(os.getcwd())

print("\n## -- -----------------\n")

print("Before creating:", os.listdir())
os.makedirs(dirname)
print("After creating", os.listdir())
print("Directory created:", dirname)

print("\n## -- -----------------\n")

os.removedirs(dirname)
print("After removing:", os.listdir())
print("Directory removed:", dirname)

print("\n## -- -----------------\n")

print("Creating text files:\n")

file = open(file_name, 'w')

print("File", file_name, "created.")

file.write("Moshiach now!!!\n")
file = open(file_name, 'r')
print(file.read())