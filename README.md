# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## How to Run Python Code with Command-Line Input

To run this project and provide input via the command line, use:

```sh
python3 main.py <path_to_book>
```

For example:
```sh
python3 main.py books/frankenstein.txt
```

If you do not provide a file path, the program will print usage instructions and exit with an error code.

## Skills Used in This Project

### 1. Command-Line Arguments
- Used `sys.argv` to read arguments passed to the script.
- Example:
  ```python
  import sys
  arg = sys.argv
  file_path = arg[1]
  ```

### 2. File Handling
- Opened and read text files using Python's `open()` function.
- Example:
  ```python
  with open(file_path) as f:
      content = f.read()
  ```

### 3. String Manipulation
- Split text into words, converted text to lowercase, and counted characters.
- Example:
  ```python
  words = text.split()
  lower_text = text.lower()
  ```

### 4. Dictionaries and Lists
- Used dictionaries to count occurrences and lists to store and sort results.
- Example:
  ```python
  mapping_dict = {}
  for char in lower_text:
      mapping_dict[char] = mapping_dict.get(char, 0) + 1
  new_dict_array = [{"char": k, "num": v} for k, v in mapping_dict.items()]
  ```

### 5. Sorting with Custom Keys
- Sorted a list of dictionaries by a specific value using the `key` parameter.
- Example:
  ```python
  def sort_on(item):
      return item["num"]
  new_dict_array.sort(reverse=True, key=sort_on)
  ```

### 6. Program Exit Codes
- Used `sys.exit(1)` to exit the program with an error code if input is missing.
- Example:
  ```python
  if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
  ```

---
This README serves as a quick reference for handling command-line input and the Python skills demonstrated in this project.
