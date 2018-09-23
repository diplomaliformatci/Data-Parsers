def normalize_contractions(tokens):
    token_map = {
        "i'm" : "i am",
        "you're" : "you are",
        "it's" : "it is",
        "we're" : "we are",
        "we'll" : "we will",
    }
    for tok in tokens:
        if tok in token_map.keys():
            for item in token_map[tok].split():
                yield item

        else:
            yield tok