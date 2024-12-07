"""
Using the previous Even_Numbers Iterator,
Write an iterator that traverses through even
numbers, but when `.history` is called all
previous iterations are returned in a list.
Remember what you've previously learned about
classes and extend the existing code to fit this
criteria.
"""

class EvenNumbers:
    history = []

    def __iter__(self):
        self.number = 0
        return self #so we can use it for def __next__

    def __next__(self):
        self.number += 2
        EvenNumbers.history.append(self.number)
        return self.number

iterator = iter(EvenNumbers())
next(iterator)
next(iterator)
next(iterator)

print(EvenNumbers.history)