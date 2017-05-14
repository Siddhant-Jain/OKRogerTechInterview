''' START OF PHASE I '''
# create a input.txt file with the text that you want to count
# and store it in the same directory as the script file
text_file=open("input.txt", "r")
com_string=text_file.read()

# lines 9-21 correspond to the interaction with the user to determine the type
# of filters that the user wants to impose with regards to the word counting
print("Do you want to ignore the case of a word [y or n] (NOTE: if you put anything other than y or n, the program will autmatically ignore case!!!)?")
answer=raw_input()
if (answer=="y"):
    com_string=com_string.lower()
else:
    com_string=com_string

print("Do you want to filter out numbers from the words counted [y or n] (NOTE: If you enter anything other than y or n, the script WILL filter out numbers from the word count)?")
print("Choosing 'y' will filter out things like dollar amounts")
num_answer=raw_input()
num_filter=True
if (num_answer=='n'):
    num_filter=False

#lines 24-64 correspond to various filters being applied to read input.txt file
filter1_string=com_string.replace("\n", " ")
filter2_string=filter1_string.replace("`", "")
filter3_string=filter2_string.replace("\x22", " ")
filter4_string=filter3_string.replace("*", " ")
filter5_string=filter4_string.replace(",", " ")
filter6_string=filter5_string.replace("?", " ")
filter7_string=filter6_string.replace(".", " ")
filter8_string=filter7_string.replace("!", " ")
filter9_string=filter8_string.replace("-", " ")
filter10_string=filter9_string.replace("\x1a", " ")
filter11_string=filter10_string.replace("(", " ")
filter12_string=filter11_string.replace(")", " ")
filter13_string=filter12_string.replace("_", " ")
filter14_string=filter13_string.replace(":", " ")
filter15_string=filter14_string.replace(";", " ")
filter16_string=filter15_string.replace("@", " ")
filter17_string=filter16_string.replace("#", " ")
filter18_string=filter17_string.replace("$", " ")
filter19_string=filter18_string.replace("%", " ")
filter20_string=filter19_string.replace("^", " ")
filter21_string=filter20_string.replace("&", " ")
filter22_string=filter21_string.replace("+", " ")
filter23_string=filter22_string.replace("=", " ")

# lines 47-57 will only run if you want to filter out numbers in the word count
if (num_filter):
    filter24_string=filter23_string.replace("1", " ")
    filter25_string=filter24_string.replace("2", " ")
    filter26_string=filter25_string.replace("3", " ")
    filter27_string=filter26_string.replace("4", " ")
    filter28_string=filter27_string.replace("5", " ")
    filter29_string=filter28_string.replace("6", " ")
    filter30_string=filter29_string.replace("7", " ")
    filter31_string=filter30_string.replace("8", " ")
    filter32_string=filter31_string.replace("9", " ")
    filter33_string=filter32_string.replace("0", " ")

if (num_filter):
    final_string=filter33_string
else:
    final_string=filter23_string

# Lines 68-71 will create a list of all the words in the text file after
# after the text file has been processed for its corresponding filters
words_list=final_string.split(" ")
parsed1_list=[elm for elm in words_list if elm!=""]
parsed2_list=[elm for elm in parsed1_list if elm!="'"]
final_parsed_list=parsed2_list

# Lines 75-80 create a dictionary with a key value pair of every words
# and its corresponding occurence
parsed_dic={}
for elem in final_parsed_list:
    if elem not in parsed_dic:
        parsed_dic[elem]=1
    else:
        parsed_dic[elem]=parsed_dic[elem]+1

# Lines 84-86 creates an output file to put the finalized word counts
# that is housed in the parsed_dic dictionary from above
output_file=open("outputPhase1.txt", "w")
for ele in parsed_dic:
    output_file.write(ele+": "+str(parsed_dic[ele])+"\n")

''' END OF PHASE I '''

''' START OF PHASE II '''

# Make sure you have installed the regex re package
import re

# restablishes a lower case version of the original text file
updated_string=final_string.lower()
words_list=final_string.split(" ")
parsed1_list=[elm for elm in words_list if elm!=""]
parsed2_list=[elm for elm in parsed1_list if elm!="'"]
final_parsed_list=parsed2_list

# establishes a boolean key for later use to see if we want to keep looking for prefixes
keep_adding_prefixes=True

# A prefix dictionary
prefix_word_count={}

# loop to keep looking for prefixes and counting
while(keep_adding_prefixes):

    # Asks for and gets the prefix from the user
    print("Please enter the prefix you are looking for")
    prefix=raw_input()
    prefix=prefix.lower()

    # Error checks the prefix received from the user
    while (prefix=="\n" or prefix==" " ):
        print("Please enter a valid string perfix")
        prefix=raw_input()
        prefix=prefix.lower()

    prefix_words=[]

    # finds and counts the words with the given prefix
    for ele in final_parsed_list:
        m=re.findall(prefix+"\w+", ele)
        if (len(m)!=0):
            prefix_words.append(m[0])

    if prefix not in prefix_word_count:
        prefix_word_count[prefix]=len(prefix_words)
    else:
        randOp=0

    prefix_words=[]

    # Asks user for more prefixes
    print("Do you want to look for more prefixes [y or n] (NOTE: If you type in any other option other that y or n, the script will not search for any other prefixes)")
    answer=raw_input()
    if (answer!="y"):
        keep_adding_prefixes=False

# outputs the results to outputPhase2.txt
output_file=open("outputPhase2.txt", "w")
for ele in prefix_word_count:
    output_file.write(ele+": "+str(prefix_word_count[ele])+"\n")

''' END OF PHASE 2 '''
