'''
Name: Nicholas Triplett

Description: Turns student data text file into an orginized csv file 

Bugs: None

Features: None

Sources: Mr. Campbell

Log: 1.0 (Latest release)
'''
fhand = open('student_data_cs2.txt')                                              #Opens the student data text file 
with open('fixed_lenght_conversion_Nicholas_Triplett.csv', 'w') as fout:          #This creates and opens the empty csv file 
    for line in fhand:                                                            #For every line in the student data text file
        fout.write(line[0:4].rstrip() + "," + line[5:19].rstrip() + "," + line[21:35].rstrip() + "," + line[36:42].rstrip() + "," + line[42:46].rstrip() + "," + line[47:58].rstrip() + "," + line[59:66].rstrip() + "," + line[67:73].rstrip() + "," + line[76:86].rstrip() + "," + line[86:87].rstrip() + "," + line[93:102].rstrip() + "," + line[102:112].rstrip() + "\n")
                                                                                  #Write into the csv file the individual data which is split by the certain indexs. For example: line[0:4] splits the first part of the line and writes it into the first box of the excel sheet.