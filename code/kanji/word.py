"""Module containing utility classes to handle Japanese word representations."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class _KanjiFragment:
    kanji: str
    offset: int
    length: int

class Word:
    """Represents a Japanese word with possible alternative kanji spellings."""

    def __init__(self, word: str, default_representation: Optional[str] = None):
        """Init method.

        Args:
            word: the kana representation of the word.
            default_representation: the common/canonical representation of the
                word when it's not in kana form. For implementation reasons,
                this is not guaranteed to match the kanji segments of the word.
        """
        self.word: str = word
        # Alternative/irregular kana spelling (like ありがとう vs ありがと)
        self.alternative: List[str] = list()
        # A segment is a list of lists of kanji fragments. Each kanji fragment
        # has a number of kanji and a starting and ending point for how many
        # characters are going to be hidden by the kanji parts.
        self.segments: List[List[_KanjiFragment]] = list()
        # The default representation is useful when we need to search for a
        # certain word in some corpus and need to match its kanji form to avoid
        # homonyms.
        self.default_representation = None
        if default_representation:
            self.default_representation = default_representation

    def add_segment(self, *fragments: Tuple(str, int, int)) -> None:
        """Adds a new segment to the word segment list.

        Args:
            fragments: series of fragments composed by a kanji string, an
                offset, and a length
        """
        segment = []
        for kanji, offset, length in fragments:
            segment.append(_KanjiFragment(kanji, offset, length))
        self.segments.append(segment)

    def add_alternative(self, word: str) -> None:
        """Adds an alternative kana representation of the word.

        Args:
            word: alternative representation of the word
        """
        self.alternative.append(word)

    def __str__(self):
        return self.word

    def _build_covered_word(self, segment: List[_KanjiFragment]) -> str:
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

    def get_all_representations(self) -> List[str]:
        """Returns a list of all possible representations of the word."""
        words = [self.word]
        words.extend(self.alternative)
        for segment in self.segments:
            words.append(self._build_covered_word(segment))
        return words

    def get_representations_with_kanji(self, kanji: str) -> List[str]:
        """Returns a list of all representations containing the given kanji."""
        words = []
        for segment in self.segments:
            found = False
            for fragment in segment:
                if kanji in fragment.kanji:
                    found = True
            if found:
                words.append(self._build_covered_word(segment))
        return words

    def get_all_kanji(self) -> List[str]:
        """Returns a list of all the kanji used all representations."""
        kanji = []
        for segment in self.segments:
            kanji.extend([x.kanji for x in segment])
        return kanji
