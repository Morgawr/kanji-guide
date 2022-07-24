"""Module for handling corpus-based analysis."""
from typing import List, Tuple, Dict

import logging


def _split_frequencies(csv_file: str) -> List[Tuple[str, int]]:
    with open(csv_file) as open_file:
        frequencies = [tuple(line.split(",")) for line in list(open_file)]
        return [(entry[0], int(entry[1])) for entry in frequencies]

class Corpus:
    """Contains corpus aggregate data like kanji and word frequency."""

    def __init__(self, kanji_frequency: str, jukugo_frequency: str):
        self._kanji_freq: Dict[str, int] = dict()
        self._jukugo_freq: Dict[str, int] = dict()
        for (kanji, freq) in _split_frequencies(kanji_frequency):
            self._kanji_freq[kanji] = freq
        for (jukugo, freq) in _split_frequencies(jukugo_frequency):
            if jukugo in self._jukugo_freq:
                logging.warning("Duplicate entry found for %s", jukugo)
                if self._jukugo_freq[jukugo] != freq:
                    logging.error("Duplicate entry has different frequency."
                                  "Found %s, expected %s.",
                                  self._jukugo_freq[jukugo], freq)
                continue
            self._jukugo_freq[jukugo] = freq

    def get_freq(self, word: str) -> int:
        """Returns the frequency of the given word.

        If the word is a single symbol, it treats it as a kanji. Othrewise it is
        considered a jukugo compound.
        """
        if len(word) == 1:
            return self._kanji_freq.get(word, 0)
        return self._jukugo_freq.get(word, 0)
