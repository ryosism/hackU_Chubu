def parseSearchResults(docs):
    parsed = []
    for doc in docs:
        parsed.append(doc.to_dict())
        
    return parsed
