# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  clean_words = remove_hyphens(words)
  long_words = remove_short_words(clean_words)
  trimmed_words = trim_word_lengths(long_words)
  return generate_output(trimmed_words)

def remove_hyphens(words):
  clean_words = []
  for word in words:
    if "-" not in word:
      clean_words.append(word)
  return clean_words

def remove_short_words(words):
  long_words = []
  for word in words:
    if len(word) > 10:
      long_words.append(word)
  return long_words

def trim_word_lengths(words):
  trimmed_words = []
  for word in words:
    if len(word)>15:
      trimmed_words.append(word[:15]+"...")
    else:
      trimmed_words.append(word)
  return trimmed_words

def generate_output(words):
  output = "These words are quite long: "
  if words:
    for word in words:
      output = output + word + ", "
    output = output[:-2]
  return output

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
