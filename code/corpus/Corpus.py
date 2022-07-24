from typing import List, Tuple, Dict

import logging

class Corpus:

    def _split_frequencies(self, csv_file: str) -> List[Tuple[str, int]]:
        with open(csv_file) as f:
            frequencies = [tuple(line.split(",")) for line in list(f)]
            return [(entry[0], int(entry[1])) for entry in frequencies]

    def __init__(self, kanji_frequency: str, jukugo_frequency: str):
        self._kanji_freq: Dict[str, int] = dict()
        self._jukugo_freq: Dict[str, int] = dict()
        for (kanji, freq) in self._split_frequencies(kanji_frequency):
            self._kanji_freq[kanji] = freq
        for (jukugo, freq) in self._split_frequencies(jukugo_frequency):
            if jukugo in self._jukugo_freq:
                logging.warning("Duplicate entry found for %s", jukugo)
                if self._jukugo_freq[jukugo] != freq:
                    logging.error(
                            "Duplicate entry has different frequency. Found %s,"
                            " expected %s.", self._jukugo_freq[jukugo], freq)
                continue
            self._jukugo_freq[jukugo] = freq

    def GetKanjiFreq(self, kanji: str) -> int:
        return self._kanji_freq.get(kanji, 0)

    def GetJukugoFreq(self, jukugo: str) -> int:
        return self._jukugo_freq.get(jukugo, 0)
