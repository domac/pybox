#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]


if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    print beer_card

    deck = FrenchDeck()
    print len(deck)

    print deck[0]

    print deck[-1]

    print choice(deck)

    print deck[:3]

    print deck[12:13]

    print '-------------'

    for card in reversed(deck):
        print card
