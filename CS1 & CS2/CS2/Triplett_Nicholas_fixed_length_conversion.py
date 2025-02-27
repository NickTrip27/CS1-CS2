'''
Name: Nicholas Triplett

Description: Turns student data text file into an orginized csv file 

Bugs: None

Features: None

Sources: Mr. Campbell

Log: 1.0 (Latest release)
'''
fhand = open('student_data_cs2.txt', 'r')                                         #Opens the student data text file 
with open('fixed_lenght_conversion_Nicholas_Triplett.csv', 'w') as fout:          #This creates and opens the empty csv file 
    for line in fhand:                                                            #For every line in the student data text file
        fout.write(line[0:4].strip() + "," + line[5:19].strip() + "," + line[21:35].strip() + "," + line[36:42].strip() + "," + line[42:46].strip() + "," + line[47:58].strip() + "," + line[59:66].strip() + "," + line[67:73].strip() + "," + line[76:86].strip() + "," + line[86:87].strip() + "," + line[93:102].strip() + "," + line[102:112].strip() + "\n")
                                                                                  #Write into the csv file the individual data which is split by the certain indexs. For example: line[0:4] splits the first part of the line and writes it into the first box of the excel sheet.