import os
import sys
import re



if len(sys.argv) != 3:
    print("USAGE: python3 get_energies_from_databases.py [SCAN results] [reference values]")
    sys.exit(1)

pawcollect = str(sys.argv[1])
reference = str(sys.argv[2])
#exceptions = str(sys.argv[3])

#lesson_number = str(sys.argv[4])
pc_list_tmp = []
pc_list = []

#? put the output from paw_collect into an array
with open(pawcollect) as f:
    for line in f:
        list_tmp = [elt.strip() for elt in line.split('/')]
        pc_list_tmp.append(list_tmp)
#? remove the first element of each subarray ['number', 'number energy']
for subarray in pc_list_tmp:
    del subarray[0]
#? split the 'number energy' entries into separate elements
for subarray in pc_list_tmp:
    subarray_tmp = [elt.strip() for elt in subarray[0].split(' ')]
    pc_list.append(subarray_tmp)
#print(pc_list)

#? put the reference file into an array while removing \t and empty strings
reference_arr = []
with open(reference) as f:
    for line in f:
        list_tmp = [elt.strip() for elt in [item.replace('\t',' ') for item in [elt.strip() for elt in line.split(' ')]][0].split(' ') if elt]
        reference_arr.append(list_tmp)
#for subarray in reference_arr:
#    subarray = [elt.strip() for elt in [item.replace('\t',' ') for item in subarray][0].split(' ') if elt]
#    reference_arr.append(subarray)
#? Calculate the energy differences between result and reference
energies = []
for arr in reference_arr:
    counter = int((len(arr)-2)/2)
    energy_tmp = 0
    for i in range(counter):
        for res in pc_list:
            if res[0] == arr[i+1]:
                energy_tmp += float(res[1])*float(arr[i+1+counter])
    energies.append(energy_tmp*627.5) #? Hartree to kcal/mol conversion
        #print(arr[i+1])
        #print(arr[i+1+counter])

#? print the difference between SCAN result and reference value
diffs = []
for i in range(len(energies)):
    diffs.append(float(energies[i])-float(reference_arr[i][-1]))

#? print the results into a file
try:
    os.remove('results')
except:
    pass

with open('results', 'a') as file:
    counter = 1
    for i in diffs:
        file.write(str(counter)+'  ')
        file.write(str(i)+'\n')
        counter += 1