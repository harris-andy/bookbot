# print("hello world")

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)

    word_count = get_number_words(text)

    character_count = get_number_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    # print(f"Character count: {character_count}")
    for key, value in character_count.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

    
def get_text(path):
     with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_number_words(text):
    words = text.split()
    return len(words)

def get_number_characters(text):
    answer = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            answer[char_lower] = answer.get(char_lower, 0) + 1
    return dict(sorted(answer.items(), key=lambda x: x[1], reverse=True))


if __name__ == "__main__":
    main()