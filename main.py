def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    ## This is the initial count of words ##
    num_words = word_counter(text)

    ## The dictionary from the earlier character count is taken here, and the sort applied ##
    characters_dict = count_characters(text)
    char_list = []
    for char, count in characters_dict.items():
        if char.isalpha():
            char_list.append({"character": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)

    print("--- Beginning report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char_data in char_list:
        print(f"The '{char_data['character']}' character was found {char_data['count']} times")
    print("--- Ending report ---")    

def word_counter(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters_dict = {}
    lowered_text = text.lower()
    for t in lowered_text:
        if t in characters_dict:
            characters_dict[t] += 1
        else:
            characters_dict[t] = 1
    return characters_dict

## Below is a secondary function needed for the dictionary sort on the value "count" ##

def sort_on(dict):
    return dict["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
