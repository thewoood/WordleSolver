def solve(searchSpace, exploredSureLetters):

  results=[]
  sureLetters = ['','','','','']
  notLetters = []
  unsureLetters = []

  entry = input('Word: ')
  print(f'y: yes \nn: no \nyn or ny: yes but not here \n'+'-'*10)
  for index, letter in enumerate(entry):
    if exploredSureLetters[index] == letter:
      print(letter+': y')
      continue
    state = input(letter + ": ")
    if state=='y':
      if exploredSureLetters[index] == '':
          exploredSureLetters[index] = letter
          sureLetters[index] = letter

    if state=='n':
      notLetters.append(letter)

    if state!='n' and state!='y':
      unsureLetters.append(str(letter+str(index+1)))
    
  uniqueUnsureLetters = list(set(map(lambda x: x[0], unsureLetters)))



  for word in searchSpace:
    shouldContinue = True
    for index, sureLetter in enumerate(sureLetters):
      if shouldContinue == False:
        break
      C_SureLetters = sureLetter != '' and word[index] != sureLetter
      C_NotLetters = any(word[index] == notletter for notletter in notLetters)
      C_UnsureLetters = any(word[int(unsureLetter[1])-1] == unsureLetter[0] for unsureLetter in unsureLetters)
      C_RemoveUnsureLetters = any(word[int(unsureLetter[1])-1] == unsureLetter[0] for unsureLetter in unsureLetters)
      C_OnlyUnsureLetters = not all(uniqeUnsureLetter in word for uniqeUnsureLetter in uniqueUnsureLetters)

      if C_SureLetters or C_NotLetters or C_UnsureLetters or C_RemoveUnsureLetters or C_OnlyUnsureLetters:
        shouldContinue = False
    if shouldContinue == True:    
      results.append(word) 
  searchSpace = results 
  return searchSpace

def main(words, steps=6):

  searchSpace = words
  exploredSureLetters=['','','','','']

  for i in range(steps):
    searchSpace = solve(searchSpace, exploredSureLetters)
    print(searchSpace)

#Example:
with open("Wordlewords.txt" , mode="r") as f:
  text = f.read()

text = text.replace("\n" , "").replace('"' , '').replace("[" , '').replace("]" , '').replace('Oa=','')

words = text.split(",")


main(words)
