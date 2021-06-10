# this progarm is made to detect racial slurs in each sentence of .txt file wich colud be useful many ways in social media
# our aim of writing racial_slurs in racial_slurs.json file is just for detection and testing purpose
# we strongly respect and maintain sincerity & we are always against profanity
import json
f = open("racial_slurs.json", 'r')
json_obj = json.load(f)


def check(scaned):
    degree = "Null"
    scaned = scaned.lower()
    for x in json_obj:
                list = json_obj[x]
                for element in list:
                    element = element.lower()
                    if element in scaned:
                        degree = x
    return degree


alphabets = "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"


def split(text):
    text = " " + text + "  "
    text = text.replace("\n", "<mark>")
    text = text.replace(".", ".<mark>")
    text = text.replace("?", "?<mark>")
    text = text.replace("!", "!<mark>")
    sentences = text.split("<mark>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


# ---------------------------------------------------------------------------------------------
while(True):
    try:
        print("Enter your choice\n1:Generate sentece profanity degree\n2:exit")
        c = int(input())
        if c == 2:
            break
        elif(c == 1):
            print('\nEnter input file name with .txt extension')
            fname = input()
            try :
                file1 = open(fname, 'r')
                file2 = open('out.txt', 'w')
                count = 0
                content = file1.read()
                counter = 0
                split_out = split(content)
                for sentence in split_out:
                    counter += 1
                    degree = check(sentence)
                    out = f"sentence: {counter}---{sentence}\nProfanity Degree : {degree}\n"
                    # print(out)
                    file2.write(out)
                file1.close()
                file2.close()
                print("\nSuccess! we have build out.txt within same folder with sentence profanity degree indication")
                print("Thnkyou so much .... Exiting....................") 
                break   
            except Exception as e:
                print('\nsomething went wrong please try again!\n')
        else:
            print('\nplease enter valid number\n')
    except Exception as e:
        print('-------------invalid input! -------------')






