from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class _KanjiFragment:
    kanji: str
    offset: int
    length: int

class Word:

    def __init__(self, word: str):
        self.word: str = word
        # Alternative/irregular kana spelling (like ありがとう vs ありがと)
        self.alternative: List[str] = list()
        # A segment is a list of lists of kanji fragments. Each kanji fragment
        # has a number of kanji and a starting and ending point for how many
        # characters are going to be hidden by the kanji parts.
        self.segments: List[List[_KanjiFragment]] = list()

    def AddSegment(self, *fragments: Tuple(str, int, int)) -> None:
        segment = []
        for kanji, offset, length in fragments:
            segment.append(_KanjiFragment(kanji, offset, length))
        self.segments.append(segment)

    def AddAlternative(self, word: str) -> None:
        self.alternative.append(word)

    def __str__(self):
        return self.word

    def _BuildCoveredWord(self, segment: List[_KanjiFragment]) -> str:
        word = ""
        index = 0
        remaining = self.word
        for fragment in segment:
            word += self.word[index:fragment.offset]
            word += fragment.kanji
            index = fragment.offset + fragment.length
            remaining = self.word[index:]
        if remaining:
            word += remaining
        return word

    def GetAllRepresentations(self) -> List[str]:
        """Returns a list of all possible representations of the word."""
        words = [self.word]
        words.extend(self.alternative)
        for segment in self.segments:
            words.append(self._BuildCoveredWord(segment))
        return words

    def GetRepresentationsWithKanji(self, kanji: str) -> List[str]:
        """Returns a list of all representations containing the given kanji."""
        words = []
        for segment in self.segments:
            found = False
            for fragment in segment:
                if kanji in fragment.kanji:
                    found = True
            if found:
                words.append(self._BuildCoveredWord(segment))
        return words

