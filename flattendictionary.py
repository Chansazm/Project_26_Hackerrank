def flatten_dictionary(dictionary):
  output = {}
  flatten_helper("", dictionary, output)
  return output

def flatten_helper(initialKey, dictionary, output):
  for key, value in dictionary.items():
    if type(value) is not dict:
      if initialKey is None or initialKey == "":
        output[key] = value
      else:
        new_key = initialKey + "." + key if key != "" else initialKey
        output[new_key] = value
    else:
      if initialKey is None or initialKey == "":
        flatten_helper(key, value, output)
      else:
        new_key = initialKey + "." + key
        flatten_helper(new_key, value, output)