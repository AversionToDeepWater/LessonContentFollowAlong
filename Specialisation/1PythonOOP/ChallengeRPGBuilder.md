# RPG Character Builder

### Description: Each student (or group) will create a set of classes representing characters, weapons, and items in a fantasy RPG. Characters will have different abilities, health levels, and weapons based on their type.

### Requirements

### 1. Base Class: Character

* Attributes: name, health, strength, defense

    * Methods:

        * attack(target: Character): Calculates damage based on the character's strength and target’s defense, then
          reduces target’s health.
        * take_damage(amount: int): Reduces the character's health by a given amount.
        * __str__: Returns a description of the character with health, strength, and other stats. (note from Hamed, you might want to google this. Its very easy)

### 2. Subclasses:

Each class inherits from Character and overrides certain methods.

#### Warrior:

* Higher strength and defense, but slower speed.
* Override attack to deal extra damage.

#### Mage:

* Lower strength, but high magical power.
* Has a cast_spell() method instead of a regular attack.

#### Archer:

* Moderate strength and high speed.
* Has a shoot_arrow() method that can hit a target from afar.

### 3. Items

(Think about what class this needs to inherit from)

* Create an Item class (for potions, shields, etc.) with attributes like name, effect, and use().

* Example:
    * Potion: Restores health.
    * shield: Temporarily boosts defense.