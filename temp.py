def dictionary_lookup(string, dictionary):

    # Remove punctionation
    if string[-1] in ["!", ".", "?"]:
        string = string.rstrip(string[-1])

    # Get words from each string
    words = string.split()
    print(words)
    
    # Check if each word is in dictionary
    x = True
    for i in words:
        if i.lower() in dictionary:
            x = True
        else:
            x = False
            break
    
    # Print the results
    print(x)
    return(x)
    
dictionary_lookup("testacseone", ["test", "case", "one"])