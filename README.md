# WordleSolver
It solves Wordle!!!


### main()
```python
def main():
    searchSpace = read_words("project/Wordlewords.txt")
    exploredSureLetters = ["", "", "", "", ""]
    program(searchSpace, exploredSureLetters, steps=6)
```
**read_words**: A function to read data (words) from Wordlewords.txt
**searchSpace**: A list of all the possible words, read from Wordlewords.txt.
**exploredSureLetters**: A list of all the green letters (the ones that we know their positions).
**program**: A function that asks the user for information and updates the list of possible words.


### program()
```python
def program(searchSpace, exploredSureLetters, steps=6):
    for i in range(steps):
        searchSpace = solve(searchSpace, exploredSureLetters)
        print(searchSpace)
        if len(searchSpace) < 2:
            sys.exit("Done!")
```
**steps**: The maximum number of times we ask user for information


### read_words()
```python
def read_words(file):
    with open(file, mode="r") as f:
        text = f.read()
        text = (
            text.replace("\n", "")
            .replace('"', "")
            .replace("[", "")
            .replace("]", "")
            .replace("Oa=", "")
        )
        words = text.split(",")
        return words
```

**file**: The name of a txt file
**replace** = Just cleaning up the txt file
**words**: After splitting words by "," ***words*** is the final list of all possible words to start with.


### solve()
```python
def solve(searchSpace, exploredSureLetters):
    results = []
    sureLetters = ["", "", "", "", ""]
    notLetters = []
    unsureLetters = []
```
**sureletters**: A list of the green letters (the ones that we know their positions).
Wait! What? Then what's the difference between ***sureLetters*** and ***exploredSureLetters***? Good point! Although it'll be better understood if we just keep explaining the other parts of the code, know that each time we ask the user for a new word, ***sureletters*** resets and becomes an empty list (to be more exact, it becomes this: \["", "", "", "", ""\]). BUT BUT BUT, ***exploredSureletters*** nevers resets and contains a list of all the green letters we've found so far.

```python
try:
        entry = input("Word: ")
    except EOFError:
        sys.exit()
        
print(f"y: yes \nn: no \nyn or ny: yes but not here \n" + "-" * 10)
```
Just asking for a new word, and catching a possible EOFError (happened when the users presses Ctrl + D)
Then guiding the user for the type of input we want. 
- **y** for a sureLetter (green ones)
- **n** for a notLetter (gray ones)
- **yn** (or anything rather than y or n) for a notSureLetter (yellow ones)


```python
for index, letter in enumerate(entry):
        if exploredSureLetters[index] == letter:
            print(letter + ": y")
            continue
```
itterating over the letters of the entry word
**if clause**: if a letter was already in exploredSureLetter (meaning we already knew it's green and where it's positioned) we don't ask the user for any extra information and jump to the next letter.


```python
state = input(letter + ": ")
```
**state**: Asks and holds the state of each letter (wether it's green, gray or yellow)

```python
if state == "y":
              exploredSureLetters[index] = letter
              sureLetters[index] = letter
```
if the the letter was a sureLetter(meaning it was green) we add it to both **exploredSureLetters** and **sureLetters**

```python
elif state == "n" and (not letter in exploredSureLetters + sureLetters):
            notLetters.append(letter)
```
else, if the letter was a notLetter (meaning it was gray) we add it to **notLetters** only if it's not in neither **exploredSureLetters** nor **sureLetters**
But why is that? We do we even bother checking the second statement?
imagine the answer to a wordle game is the word **alone**. also suppose that you enter the word **leone** as an input. Let's check step by step, what will happen. 
First, when you enter leone in wordle game, it will show you these colors:
- l: yellow (because there's an L in ALONE, but it's not quite in right place)
- e: gray! (wait, why gray, ALONE does have an E! yeah, you're right, but let me explain this later)
- o: green (horray!)
- n: green
- e: green

Now take your time and think about why first E we input was gray...
Yes! Beacuse if we've enter E also as our last letter, then we've already found the one and only E which exists in the word ALONE! Then why should Wordle tell us that there's an E but you misplaced it. We've found it, there's no other E in the word ALONE. so the first E we've entered is absoloutely wrong.

So, now take a deep breath while we get back to our Main Qustion! 
> (But why is that? We do we even bother checking the second statement?)
Now suppose that the users tell us that the first e was gray. the typically what we would do is adding the letter e to the notLetters list. so the next time we filter our searchSpace, we'll omit all the words containing e. But wait! Doesn't this mean that we'll also omit the word alone (which is the correct answer) from our list? Well, yes! beacuse Alone has an E and we tell the programm to delete any word containing any number of E(s). 
So what should we do? It's when our mysterious STATEMENT comes in. It checks wether the gray letter was ever input as a sureLetter or not. If yes, we don't add the letter to the notLetters list, cause we don't want it to be removed. And if it was not a sureLetter, we simply add it to notLetters to get rid of it!


