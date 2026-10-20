def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # ite code here
    new_list=[]
    for i in tokens:
        if i in stopwords:
            pass
        else:
            new_list.append(i)
    return new_list