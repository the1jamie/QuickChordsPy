notes = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

def findRoot(key):
  for note in notes:
    if notes[0] != key:
      notes.append(notes.pop(0))
  return notes


      
def getChord(bass_note):
  return list(chords[bass_note]())


def one():
  return map(notes.__getitem__,[0,4,7])
def two():
  return map(notes.__getitem__,[0,5,9])
def three():
  return map(notes.__getitem__,[2,4,7])
def four(): 
  return map(notes.__getitem__,[0,5,9])
def five():
  return map(notes.__getitem__,[3,7,11])
def six():
  return map(notes.__getitem__,[0,4,7])
def seven():
  return map(notes.__getitem__,[3,7,11])

chords = {
  1: one,
  2: two,
  3: three,
  4: four,
  5: five,
  6: six,
  7: seven
}

def quickChords(bassNote, chords):
  findRoot(bassNote)
  return (bassNote, getChord(chords))

print(quickChords("E", 7))