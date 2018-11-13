f = open('FrenchSMScorpus.txt', 'rU')
text = f.read()
SMSlist = text.split('<SMS>')
f.close()

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