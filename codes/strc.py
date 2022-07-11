import os
import sys
import pprint

inputfile = str(sys.argv[1])
output = str(sys.argv[2])
str_list = []

#file into array
with open(inputfile) as f:
    for line in f:
        list_tmp = [elt.strip() for elt in line.split('\n')]
        str_list.append(list_tmp)
#str_list will contain only the coordinates and the element identifier
str_list = str_list[1:-1]

#split the coordinates and the element identifiers from each other
#print(len(str_list))
tmp = []
tmp2 = []


for i in range(len(str_list)):
    #print(str_list[i][0])
    tmp2.append([x.strip() for x in str_list[i][0].split(' ')])
for j in range(len(tmp2)):
    for k in range(len(tmp2[j])):
        #print(tmp2[j][k])
        try:
            if float(tmp2[j][k]) or float(tmp2[j][k]) == 0.0:
                tmp.append(tmp2[j][k])
                #tmp[j][k] += tmp2[j][k]
                #print('hi')
        except:
            pass
#split tmp into chunks of 3 corresponding to the original coordinates
tmp = [tmp[i:i+3] for i in range(0,len(tmp),3)]
#add the correct identifiers to the array tmp
for element in range(len(tmp)):
    tmp[element].append(tmp2[element][-1])

#print('str_list=',str_list)
#tmp stores the clean positions of the atoms including the identifiers ONLY
#print('tmp2=',tmp2)
#print('tmp=',tmp)


#create a unique list of all identifiers
identifiers = []
for i in range(len(str_list)):
    if tmp[i][-1].capitalize() not in identifiers:
        identifiers.append(tmp[i][-1].capitalize())

#print(identifiers)
#write the structure file
try:
    os.remove(output)
except OSError:
    pass
with open(output, 'a') as file:
    file.write('!STRUCTURE')
    file.write('\n')
    file.write('    !GENERIC LUNIT=1.889726124 !END')
    file.write('\n')
    file.write('    !OCCUPATIONS EMPTY=5 !END')
    file.write('\n')
    file.write('    !LATTICE T= 0.00000 15.00000 15.00000')
    file.write('\n')
    file.write('                15.00000 0.00000 15.00000')
    file.write('\n')
    file.write('                15.00000 15.00000 0.0000 !END')
    file.write('\n')
    for j in range(len(identifiers)):
        if 'H' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=3. NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'O' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=15.999 ZV=6 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'N' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=14.0067 ZV=5 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'C' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=12.0107 ZV=4 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'Li' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'\' ID=\''+identifiers[j]+'_.75_6.0\' M=6.941 ZV=1 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'Si' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'\' ID=\''+identifiers[j]+'_.75_6.0\' M=28.0855 ZV=4 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'Be' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'\' ID=\''+identifiers[j]+'_.75_6.0\' M=9.012182 ZV=2 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'B' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=10.811 ZV=3 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'P' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=30.973762 ZV=5 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'S' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=32.065 ZV=6 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'Cl' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'\' ID=\''+identifiers[j]+'_.75_6.0\' M=35.453 ZV=7 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'Al' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'\' ID=\''+identifiers[j]+'_.75_6.0\' M=26.981539 ZV=3 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'F' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'_\' ID=\''+identifiers[j]+'_.75_6.0\' M=18.998 ZV=7 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'Na' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'\' ID=\''+identifiers[j]+'_.75_6.0\' M=22.989 ZV=1 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
        elif 'Mg' == identifiers[j].capitalize():
            file.write('!SPECIES NAME=\''+identifiers[j].capitalize()+'\' ID=\''+identifiers[j]+'_.75_6.0\' M=24.305 ZV=2 NPRO=1 0 0 LRHOX=4    !END')
            file.write('\n')
    for i in range(len(tmp)):
            file.write('!ATOM   NAME= \''+tmp[i][-1].capitalize()+'_'+str(i+1)+'\' R= '+str(tmp[i][0])+' '+str(tmp[i][1])+' '+str(tmp[i][2])+' !END')
            file.write('\n')
    file.write('    !ISOLATE_X !END')
    file.write('\n')
    file.write('!END')
    file.write('\n')
    file.write('!EOB')

