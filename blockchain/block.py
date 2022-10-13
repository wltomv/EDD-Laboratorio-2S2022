
from dataclasses import dataclass

# Author: "Walter Mach, @wltomv"
# Copyright: "Copyright 2022, EDD"
# Credits: ["Walter Mach"]

# TODO add rootmerkle


@dataclass
class Block:
    timestamp: str
    nonce: int
    previoushash: str
    hash: str
    index: int

    def __init__(self, data, timestamp, nonce, previoushash, hash, index) -> None:
        self.data = data
        self.timestamp = timestamp
        self.nonce = nonce
        self.previoushash = previoushash
        self.hash = hash
        self.index = index

        self.next = None


@dataclass
class Data:
    _from: str
    skins: list

    def __init__(self, _from, skins) -> None:
        _from = _from
        skins = skins
