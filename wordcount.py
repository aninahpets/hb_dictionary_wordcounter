def get_word_count(path):
    poem = open(path)
    #set file to variable poem
    word_count = {}
    #created a new dictionary for our words
    for line in poem:
        #iterating over each line in the file
        newline = line.strip()
        #stripping whitespace off each line
        words = newline.split()
        #splitting on whitespace in each line to get list of words on each line
        for word in words:
            #iterating over each list of words (previously lines)
            word_count[word] = word_count.get(word, 0) + 1
            #within new dictionary, assigning key and using .get method to retrieve current word count and add 1 (default to zero if none)
    for word, count in word_count.items():
        #iterate over completed dictionary
        print word, count
        #print key and value


get_word_count("twain.txt")