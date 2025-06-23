def count_words(text):
  words = text.split()
  return len(words)

def count_unique_words(text):
  lower_text = text.lower()

  mapping_dict = {}
  for char in lower_text:
    if char in mapping_dict:
      mapping_dict[char] += 1
    else:
      mapping_dict[char] = 1

  return mapping_dict

def restruct_dict_to_array(mapping_dict):
  new_dict_array = []
  for key in mapping_dict:
    new_dict_array.append({"char": key, "num": mapping_dict[key]})

  new_dict_array.sort(reverse=True, key=sort_on)
  return new_dict_array

def sort_on(items):
  return items["num"]