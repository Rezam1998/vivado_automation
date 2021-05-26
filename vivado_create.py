import os
import sys

print(f"Argument Count: {len(sys.argv)}")
for i , arg in enumerate(sys.argv):
	print(f"Argument {i:>6}: {arg}")

file_name = sys.argv[1]
dir_path = os.path.dirname(os.path.realpath(__file__))
print(file_name)
print(dir_path)

vivado_cmd = "C:\\Xilinx\\Vivado\\2018.3\\bin\\vivado.bat"
cmd = " -mode batch -source " + dir_path + "\\" + file_name
print(cmd)
os.system(vivado_cmd + cmd)
# os.system(cmd)