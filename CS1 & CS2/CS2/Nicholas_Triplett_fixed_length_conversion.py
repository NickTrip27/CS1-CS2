fhand = open('student_data_cs2.txt')
with open('dic.csv', 'w') as fout:
    for line in fhand:
        fout.write(line[0:4].rstrip() + "," + line[5:19].rstrip() + "," + line[21:35].rstrip() + "," + line[36:42].rstrip() + "," + line[42:46].rstrip() + "," + line[47:58].rstrip() + "," + line[59:66].rstrip() + "," + line[67:73].rstrip() + "," + line[76:86].rstrip() + "," + line[86:87].rstrip() + "," + line[93:102].rstrip() + "," + line[102:112].rstrip() + "\n")
    