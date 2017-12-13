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


class Character(object):
    """A Character for an RPG.

    Can choose from physical type fighters and magical type fighters.
    """

    def __init__(self, arg):
        """Create a character."""
        self.arg = arg
