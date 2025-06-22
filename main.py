from stats import count_words, count_unique_words

def main():
  file_path = "books/frankenstein.txt"
  book_text = get_book_text(file_path)
  word_count = count_words(book_text)
  unique_words = count_unique_words(book_text)
  print(unique_words)

def get_book_text(file_path):
  file_content = ""
  with open(file_path) as f:
    file_content = f.read()
  return file_content

#  This code reads the content of a book file and prints it to the console.
main()