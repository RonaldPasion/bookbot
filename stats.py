def count_words(text):
    return len(text.split())

def count_chars(text):
    count = {}
    for i in text.lower():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count