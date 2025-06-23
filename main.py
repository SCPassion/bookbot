from stats import count_words, count_unique_words, restruct_dict_to_array

def main():
  file_path = "books/frankenstein.txt"
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

def get_book_text(file_path):
  file_content = ""
  with open(file_path) as f:
    file_content = f.read()
  return file_content

#  This code reads the content of a book file and prints it to the console.
main()