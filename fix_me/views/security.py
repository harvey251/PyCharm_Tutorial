def secure_function():
    return {
        "In The house": "Not this",
        "Over The Hill": [
            ToadScerurity.from_here,
            ToadScerurity.eating_bananna_cake,
            ToadScerurity.away
        ],
        "Under the bed": "Not this"
    }


class ToadScerurity:
    @property
    def away(self):
        return "456"

    @property
    def from_here(self):
        return "343"

    @property
    def eating_bananna_cake(self):
        return "666"