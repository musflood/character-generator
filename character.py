"""RPG Character Generator.

Build a Character object that has some attributes and stats
characteristic of RPG characters. As a starting point, characters
tend to have some number of hit points that corresponds to their
health. They may have other stats that will augment their abilities,
like Strength, Intelligence, Dexterity, Luck, etc. Look at the
character generators for Dungeons & Dragons if you need an idea
https://orcpub2.com/

Physical fighters tend to have stamina which determines how often,
how hard, or how fast they can attack. Stronger attacks consume more
stamina. They can equip weapons and armor, have certain abilities for
special attacks, that type of thing. Their power tends to be augmented
chiefly by strength

Magical fighters tend to have magic points (MP) which determine how
much magic they can use. Stronger spells consume more MP. Their power
tends to be augmented chiefly by Intelligence. They typically equip
magic wands or staves, and wear robes and such that augment their
intelligence.

Use that as a basis and build up your character generator from there.
When the generator is done it should print the basics of the character
out to the terminal, listing their stats and abilities if they have any.
"""
import random


class Character(object):
    """A Character for an RPG.

    Can choose from physical type fighters and magical type fighters.
    """

    CLASSES = {
        'Barbarian': [12, ['simple', 'martial']],
        'Bard': [8, ['simple', 'crossbow-hand', 'longsword', 'rapier', 'shortsword']],
        'Fighter': [10, ['simple', 'martial']],
        'Monk': [8, ['simple', 'shortsword']],
        'Paladin': [10, ['simple', 'martial']],
        'Ranger': [10, ['simple', 'martial']],
        'Rogue': [8, ['simple', 'crossbow-hand', 'longsword', 'rapier', 'shortsword']],
        'Cleric': [8, ['simple']],
        'Druid': [8, ['dagger', 'sickle', 'spear', 'mace', 'quarterstaff', 'sling', 'javelin', 'club', 'scimitar', 'dart']],
        'Sorcerer': [6, ['dagger', 'dart', 'sling', 'quarterstaff', 'crossbow-light']],
        'Warlock': [8, ['simple']],
        'Wizard': [6, ['dagger', 'dart', 'sling', 'quarterstaff', 'crossbow-light']]
    }

    def __init__(self, class_type=None):
        """Create a character."""
        self.str = random.randint(6, 19)
        self.dex = random.randint(6, 19)
        self.con = random.randint(6, 19)
        self.int = random.randint(6, 19)
        self.wis = random.randint(6, 19)
        self.cha = random.randint(6, 19)

        if not class_type:
            self.class_type = random.choice(list(self.CLASSES))
        else:
            if class_type not in self.CLASSES:
                raise ValueError('That is not a class you can choose.')
            self.class_type = class_type

        self.setup_class()

    def setup_class(self):
        """Edit stats based on class."""
        base_hp = self.CLASSES[self.class_type][0]
        self.hp = base_hp + self.con
        self.weapons = self.CLASSES[self.class_type][1]


if __name__ == '__main__':
    print('Generate a simple RPG character!')
    print('Possible classes are:')
    for cl in Character.CLASSES:
        print(cl)
    class_type = input('Choose a class, or leave blank for random: ')
    char = Character(class_type)
    print("""Your character is:
    --- {} ---
    HP: {}

    STR: {}
    DEX: {}
    CON: {}
    INT: {}
    WIS: {}
    CHA: {}

    Weapon Proficiencies: {}
""".format(char.class_type, char.hp, char.str, char.dex, char.con, char.int,
           char.wis, char.cha, ', '.join(char.weapons)))
