def parseSearchResults(docs):
    parsed = []
    for doc in docs:
        parsed.append(doc.to_dict())

    import pdb; pdb.set_trace()

    return parsed