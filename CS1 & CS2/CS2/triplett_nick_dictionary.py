'''

Name: Nicholas Triplett

Description: Opens a file and removes any unnessesary words before sorting the file and creating a pie chart for the most used words 

Bugs: Shouldn't be any bugs 

Features: None

Sources: W3 Schools - https://www.w3schools.com/ - Python for Everybody - Book - GeeksforGeeks - https://www.geeksforgeeks.org/ - Stack Overflow - https://stackoverflow.com/ - Jeremy Morgan - https://www.jeremymorgan.com/

Log: 1.0 (latest release)

'''

import re                           #Imports the re module
import matplotlib.pyplot as plt     #Imports matplotlib module and sets it to plt 
import pandas as pd                 #Imports pandas module and sets it to pd




def word_count(fhand):
    """
    Creates a dictionary from the entered file and then sorts it, and returns a pie chart. 

    Args:
        fhand(str): The file that wants to be inputed 

    Returns:
        Bool: A pie chart of words used more then 10 times. 

    """
    
    
    unnecessarywords = ['never','year','time','tonight','by','going','from','been','them','more','new','no','am','your','than','every','were','ever','or','can','its','these','make','other','now','also','her','which','most','way','any','into','just','im','and','the','to','of','i','a', 'in', 'for', 'our', 'we', 'that', 'is', 'he', 'are', 'will', 'who', 'who', 'my' , 'with', 'us', 'be', 'as', 'she', 'not', 'you', 'on', 'it', 'this', 'trump', 'an', 'when', 'have', 'has', 'but', 'would', 'people', 'was', 'one', 'their', 'me', 'all', 'know', 'they', 'his', 'about', 'up', 'at', 'because', 'out', 'what', 'so']
    counts = dict()                                 #Creates a dictionary 
    for line in fhand:                              #Scans each line in the file 
        line = line.lower()                         #Sets the file to line and makes all the characters lowercase
        words = line.split()                        #Sets the line variable as words and splits the entire string into a list of words
        
        for word in words:                          #for each word in the list words
            word = re.sub(r'[^\w\s]', '', word)     #this function substitutes each non-word character which is punctuation and white space with an empty string 
            
            if word not in unnecessarywords:        #If a word in the list words is not in the list unnecessarywords
                if word not in counts:              #If the word not the dictionary, set 1 to it 
                    counts[word] = 1
                else:
                    counts[word] += 1               #If the word is in the dictionary, add one it it 
    

    sorted_dict = dict(sorted(counts.items(), key=lambda item:item[1], reverse = True))     #Sort by value in ascending order through reverse true



    with open('Graphing_dict.csv','w') as fout:     #Opens a excel file and sets it to fout
        fout.write('Word' "," 'Amount' + "\n")      #Write in the file the titles of the first two columns 
        for key, value in sorted_dict.items():      #sets the key to the word sorted value, and sets the value to the item or the number 
            
            if value >= 10:                         #If the number(value) of a number is greater than 10 
                fout.write(key + "," + str(value) + "\n")   #Write in the csv file the key (or the word), and then put in the value (number which is set to a string, and finally enter)
    
    df =  pd.read_csv('Graphing_dict.csv')          #This function reads the csv file which is entered and sets it to df 
    word_data = df["Word"]                          #Reads the column Word
    amount_data = df["Amount"]                      #Reads the column Amount
    
    plt.pie(amount_data, labels=word_data, autopct='%1.1f%%',startangle=90)     #Creates the pie chart at using the variables set above, starts the chart at 90 degrees, and then shows the percentages of each amount through autopc
    plt.title("Amount of times each word is used starting from nine.")          #Sets the title to the chart 
    plt.show()                                                                  #Display's all open figures and shows the pie chart 
                                                                   
    
    

fhand = open('cleaned_trump_speech_transcript.txt')                             #Sets fhand to the file that will be opened 
word_count(fhand)                                                               #Runs the function word count with the file perameter 
fhand = open('kamala_new.txt')                                                  #Sets fhand to the file that will be opened 
word_count(fhand)                                                               #Runs the function word count with the file perameter 







    
                                







