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

def sort_on(items):
    return items["num"]
    
def sorted_list(character):
    result = []
    
    for key, value in character.items():
        if key.isalpha():
            result.append({"char": key, "num": value})
    
    result.sort(reverse=True, key=sort_on)
    return result
