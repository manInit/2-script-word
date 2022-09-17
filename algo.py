import pymorphy2
import math

morph = pymorphy2.MorphAnalyzer()

def norm(x):
    p = morph.parse(x)[0]
    return p.normal_form

def trimNonLetter(word):
  while word and not word[-1].isalpha():
    word = word[:-1]
  while word and not word[0].isalpha():
    word = word[1:]
  return word

def sortDictByValue(dict):
  return { k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True) }

def countWord(text, progress):
  words_count = {}
  words = text.split()
  count_all = len(words)
  count = 0

  for word in words:
    word = word.lower()
    word = trimNonLetter(word)
    p = morph.parse(word)[0]
    if p.tag.POS == 'CONJ' or p.tag.POS == 'PREP' or p.tag.POS == 'PRCL' or p.tag.POS == 'NPRO':
      count_all -= 1
      continue
   
    word = norm(word)
   
    if word == '':
      count_all -= 1
      continue
    
    if word in words_count:
      words_count[word] += 1
    else:
      words_count[word] = 1
    count += 1

    progress.setValue(math.floor(count / count_all * 100))
  return words_count, count

def countEquelsWords(inputText, progress):
  progress.setValue(0)
  words_count, count = countWord(inputText, progress)
  words_count = sortDictByValue(words_count)

  res = 'Всего: ' + str(count) + '\n'
  for key, value in words_count.items():
    res += key + ' - ' + str(value) + '\n'
  progress.setValue(100)
  return res