def joinwords(listoflist):
    convolist = []
    for item in listoflist:
        uttlist = []
        for subitem in item:
            uttlist.append(' '.join(subitem))
        convolist.append(uttlist)
    return convolist
