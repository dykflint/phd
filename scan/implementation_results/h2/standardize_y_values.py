from decimal import Decimal
import sys

def create_array_from_file(file):
    tmp_arr = []
    with open(file, 'r') as qfile:
        for line in qfile:
            line_tmp = [elt.strip() for elt in line.split(' ') if line != '\n']
            #! skip iteration if array is empty
            if len(line_tmp) == 0: continue
            tmp_arr.append(line_tmp)
    return tmp_arr

if len(sys.argv) != 3:
    print("USAGE: python3 standardize_y_values.py [file (format: x-value y-value)] [reference value]")
    exit(1)

results_file = str(sys.argv[1])
reference_value = Decimal(sys.argv[2])

results = create_array_from_file(results_file)

print(results)

with open(results_file+"_mod", "a") as file:
    for i in range(len(results)):
        file.write(results[i][0] + " " + str(Decimal(results[i][1])-reference_value) + "\n")
