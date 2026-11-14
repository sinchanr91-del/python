def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List has first/last character same", lst)

    return ctr
count = match_words(['17','141','ASD','WeW','ABA','53325','ambika'])
print("Number of words of first/last character same:",count)


    
