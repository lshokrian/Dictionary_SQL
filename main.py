import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
def lookUpWord(word):
    word = word.lower()
    #grab the word
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    results = cursor.fetchall()
    if results:
        return results
#       for result in results:
#           print("\t - " + result[1])
    else:
        #check if capital of word was met
        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word.upper())
        results = cursor.fetchall()
        if results:
            return results
 #           for result in results:
 #               print("\t - " + result[1])
        else:
            #check if word is an acronym
            query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word.capitalize())
            results = cursor.fetchall()
            if results:
                return results
#               for result in results:
#                   print("\t - " + result[1])
            else:
                #check if different word was meant
                query = cursor.execute("SELECT * FROM Dictionary")
                results = cursor.fetchall()
                allWords = []
                for result in results:
                    allWords.append(result[0])
                possibleWords = get_close_matches(word, allWords, 3)
                if (len(possibleWords) > 0):
                    for possibleWord in possibleWords:
                        yesOrNo = input("Did you mean " + possibleWord + "?")
                        if (yesOrNo.lower() == "y" or yesOrNo.lower() == "yes"):
                            query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % possibleWord)
                            results = cursor.fetchall()
                            if results:
                                return results
#                               for result in results:
#                                   print("\t - " + result[1])


def printResults(results):
    if (results):
        for result in results:
            print("\t - " + result[1])
    else:
        print("Sorry word not found")



print("Welcome to the Dictionary")
userInput = input("Enter a word you'd like to look up: ")
#print(lookUpWord(userInput))
printResults(lookUpWord(userInput))
