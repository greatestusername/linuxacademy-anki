import random
import itertools
import genanki
import json

def get_model(css):
    return genanki.Model(
        1607392319,
        'Simple Model',
        fields = [
            {'name': 'Front'},
            {'name': 'Back'},
        ],
        templates = [
            {
                'name': 'Card 1',
                'qfmt': '<div id="front">{{Front}}</div>',
                'afmt': '{{FrontSide}}<hr id="back"><div id="back">{{Back}}</div>',
            },
        ],
        css = css)


def new_deck(deck_name):
    random.seed(hash(deck_name))
    deck_id = random.randrange(1 << 30, 1 << 31)
    return genanki.Deck(deck_id, deck_name)

class Card(genanki.Note):
    @property
    def guid(self):
        return genanki.guid_for(self.fields[0]) # Front Side

def new_card(model, front, back):
    return Card(
        model = model,
        fields = [front, back]
    )

def main():

    # read in the input json data (a flat array of objects) for our cards
    with open("resources/AWS-Cards.json") as json_data:
        cards = json.load(json_data)
    with open("resources/cards.css") as cssData:
        card_style = cssData.read()
    
    decks = []
    model = get_model(card_style)
    for ca in cards:
        print("front is: \'" + ca['front'] + "\' --- and back is: \'" + ca['back'] + "\'")
        # :: has special meaning in Anki card names: it nests decks.
        deck_name = "AWS-ArchPro-2019-Linux-Academy"
        print("creating... " + deck_name)
        deck = new_deck(deck_name)
        card = new_card(model, ca['front'], ca['back'])
        deck.add_note(card)
        decks.append(deck)
    genanki.Package(decks).write_to_file('dist/aws-archpro-2019.apkg')

if __name__ == "__main__":
    main()

