from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class _KanjiSegment:
    kanji: str
    length: int

class Word:

    def __init__(self, word: str):
        self.word: str = word
        # A segment is a list of kanji segments. Each kanji segment has a
        # length which covers how much of the word is hidden by the kanji.
        self.segments: List[_KanjiSegment] = list()

    def AddSegment(self, kanji: str, length: int) -> None:
        self.segments.append(_KanjiSegment(kanji, length))

    def __str__(self):
        return self.word

    def _BuildCoveredWord(self, segment: _KanjiSegment) -> str:
        if segment.length >= len(self.word):
            return segment.kanji
        else:
            return segment.kanji + self.word[segment.length:]

    def GetAllRepresentations(self) -> List[str]:
        """Returns a list of all possible representations of the word."""
        words = [self.word]
        for segment in self.segments:
            words.append(self._BuildCoveredWord(segment))
        return words

    def GetRepresentationsWithKanji(self, kanji: str) -> List[str]:
        """Returns a list of all representations containing the given kanji."""
        words = []
        for segment in self.segments:
            if kanji in segment.kanji:
                words.append(self._BuildCoveredWord(segment))
        return words

