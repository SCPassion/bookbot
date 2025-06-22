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