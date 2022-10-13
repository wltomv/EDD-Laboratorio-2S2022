from datetime import datetime
from multiprocessing.forkserver import main
from block import *

# Author: "Walter Mach, @wltomv"
# Copyright: "Copyright 2022, EDD"
# Credits: ["Walter Mach"]


class Blockchain:
    def __init__(self) -> None:
        self.genesis = None
        self.actual = None

    def get_index(self):
        return self.actual.index + 1 if self.actual else 0

    def get_previoushash(self):
        return self.actual.hash if self.actual else '-1'

    # TODO include the proof of work code
    def proof_of_work(self, timestamp, previoushash):
        return {'nonce': 35, 'hash': '0000x23dlxo....'}

    def insertBlock(self, _from, skins):
        data = Data(_from, skins)
        timestamp = datetime.now().strftime("%d-%m-%Y::%H:%M:%S")
        previoushash = self.get_previoushash()

        proof = self.proof_of_work(timestamp, previoushash)
        new = Block(data, timestamp, proof['nonce'],
                    previoushash, proof['hash'], self.get_index())

        if self.genesis == None:
            self.genesis = new
            self.actual = self.genesis
        else:
            self.actual.next = new
            self.actual = new

    def __repr__(self):
        rep = "[\n"
        aux = self.genesis
        while aux is not None:
            rep += '\t'
            rep += f'{aux},' if aux.next != None else f'{aux}'
            rep += '\n'
            aux = aux.next
        rep += "]"
        return rep
