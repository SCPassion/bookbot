import sys
from stats import count_words, count_unique_words, restruct_dict_to_array, get_book_text

def main():
  arg = sys.argv

  if(len(arg) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  file_path = arg[1]
  book_text = get_book_text(file_path)
  word_count = count_words(book_text)
  unique_words = count_unique_words(book_text)
  words_count_array = restruct_dict_to_array(unique_words)

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for dict in words_count_array:
    if dict["char"].isalpha():
      print(f"{dict["char"]}: {dict["num"]}")

#  This code reads the content of a book file and prints it to the console.
main()