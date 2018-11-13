# Download the 88milSMS corpus as .ods from http://88milsms.huma-num.fr/corpus.html (You need to enter credentials).
# You want the corpus in a .txt file with the following format: The content of each SMS followed by <SMS>, in order to separate each SMS.
# You can do this by adding a column in Excel to the right of the SMS_ANON column, and filling that column with the text <SMS> in every cell.
# Then copy those two columns to a .txt file, name it FrenchSMScorpus.txt, and put it in your working directory.

f = open('FrenchSMScorpus.txt', 'rU') # Open the .txt file
text = f.read()
SMSlist = text.split('<SMS>') # Separate the corpus so each SMS is an item in a list. Make sure you've followed the instructions in the comments above.
f.close()

# This script allows you to enter a search term, and it prints the number of SMS that contain that term as well as the full text of the first 5 SMS that contain it.
searchterm = 'searchterm'
i = 5
while searchterm != 'exit':
    while i > 4:
        searchterm = input('Enter an expression to search: ')
        ST = [searchterm]
        stcount = sum(any(m.lower() in L.lower() for m in ST) for L in SMSlist)
        SMScount = len(SMSlist)
        stpercentage = round(100*stcount/SMScount, 2)
        print(f'"{searchterm}" is found in {stcount} of {SMScount} text messages. ({stpercentage}%)')
        print('Here are some examples:')
        i = 0
    
    while i < 4:
        for text in SMSlist:
            if searchterm.lower() in text.lower():
                print(f'{i+1}: {text}')
                i += 1
                if i > 4:
                    break
