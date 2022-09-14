EN_VOWELS = 'aeiouy'
RU_VOWELS = 'яиюэоаыуеё'

def trimNonLetter(word):
  while word and not word[-1].isalpha():
    word = word[:-1]
  while word and not word[0].isalpha():
    word = word[1:]
  return word

def sortDictByValue(dict):
  return { k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True) }

def deleteVowels(word):
  if len(word) > 2 and (word[-1] in EN_VOWELS or word[-1] in RU_VOWELS):
    word = word[:-1]
  return word

def countWord(text):
  words_count = {}
  words = text.split()
  count = 0

  for word in words:
    word = word.lower()
    word = trimNonLetter(word)
    # word = deleteVowels(word)
    if word == '':
      continue
    
    if word in words_count:
      words_count[word] += 1
    else:
      words_count[word] = 1
    count += 1
  return words_count, count

def countEquelsWords(inputText):
  words_count, count = countWord(inputText)
  words_count = sortDictByValue(words_count)

  res = 'Всего: ' + str(count) + '\n'
  for key, value in words_count.items():
    res += key + ' - ' + str(value) + '\n'

  return res