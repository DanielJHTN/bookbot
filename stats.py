def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
        
def sort_on(characters):
    return characters["num"]
    
def sort_characters(text):
    char_count  = get_num_characters(text)
    count_list = [{"char": char, "num": count} for char, count in char_count.items()]
    count_list.sort(reverse=True, key=sort_on)
    return count_list