# V 1.3

import random, sys

class Monster:

   def __init__(self, possesions, probability, strength, dexterity, constitution, weapon, armor, name, description):
        self.possesions = possesions
        self.probability = probability
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.hitPoints = self.constitution * 2
        self.currentHitPoints = self.hitPoints
        self.weapon = weapon
        self.armor = armor
        self.ac = 0
        self.name = name
        self.description = description
        self.blocked = None
        

   def attack(self):
      print('The ' + self.name + ' attacks you with its ' + self.weapon.name + '.')
      attackRoll = random.randint(1, 20)
      attackRoll = attackRoll + self.dexterity
      if attackRoll > character.ac:
         print('It hits!')
         damage = random.randint(1, self.weapon.damageRoll)
         damage = damage + self.strength
         character.currenthp = character.currenthp - damage
         print('It does ' + str(damage) + ' damage.')
      else:
         print('It misses!')

   def checkForDeath(self):
      if (self.currentHitPoints <= 0):
         print('You kill it!')
         self.dropItems()
         character.currentMonster = None
         return True
      else:
         return False

   def equipArmor(self, armor):
      self.armor = armor
      self.ac = self.armor.hardness

   def dropItems(self):
      if (len(self.possesions) > 0):
         for i in range(len(self.possesions)):
            item = self.possesions[i]
            x = random.randint(1, 200)
            if x <= self.probability[i] + character.luck:
               character.currentRoom.items.append(item)
               print('It drops a: ' + item.name)

class Character:
    
   def __init__(self, strength, dexterity, constitution, intelligence, luck, stamina):
        self.inventory = []
        self.currentRoom = None
        self.currentMonster = None
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.luck = luck
        self.stamina = stamina
        self.cc = self.stamina * 5
        self.currentcc = 0
        self.hp = self.constitution * 3
        self.ac = 0
        self.currenthp = self.hp
        self.weapon = None
        self.armor = None

   def attack(self):
      print('You attack the ' + self.currentMonster.name + ' with your ' + self.weapon.name + '.')
      attackRoll = random.randint(1, 20)
      attackRoll = attackRoll + self.dexterity
      if (attackRoll > self.currentMonster.ac):
         print('You hit!')
         damage = random.randint(1, self.weapon.damageRoll)
         damage = damage + self.strength
         self.currentMonster.currentHitPoints = self.currentMonster.currentHitPoints - damage
         print('You do ' + str(damage) + ' damage.')
      else:
         print('You miss!')

   def calculateWeight(self):
      itemWeight = 0
      for i in range(len(self.inventory)):
         x = self.inventory[i].weight
         itemWeight = itemWeight + x
      return itemWeight

   def addItem(self, item):
        self.inventory.append(item)

   def removeItem(self, item):
        self.inventory.remove(item)
        if (item == self.weapon):
           self.weapon = None
        if (item == self.armor):
           self.armor = None
           self.ac = 0
           
   def printItems(self):
        if (len(self.inventory) > 0):
            print('Inventory:')
            for i in range(len(self.inventory)):
                item = self.inventory[i]
                if (item == self.weapon):
                   print(item.name + ' <equipped> (' + str(item.weight) + ')')
                elif (item == self.armor):
                   print(item.name + ' <equipped> (' + str(item.weight) + ')')
                else:
                   print(item.name + ' (' + str(item.weight) + ')')
        else:
           print('You have nothing in your inventory')
           
   def getItems(self):
       return self.inventory

   def setMonster(self, monster):
      self.currentMonster = monster

   def printMonster(self):
        if (self.currentMonster):
           if self.currentMonster.hitPoints - self.currentMonster.currentHitPoints != 0:
              hpLost = '(-' + str(self.currentMonster.hitPoints - self.currentMonster.currentHitPoints) + ')'
           else:
              hpLost = ''
           print('There is a ' + self.currentMonster.name + hpLost + ' blocking the ' + self.currentMonster.blocked + ' exit.')

   def equipArmor(self, armor):
      self.armor = armor
      self.ac = self.armor.hardness

   def equipWeapon(self, weapon):
      self.weapon = weapon

   def checkForDeath(self):
      if character.currenthp <= 0:
         print('You died!')
         self.currenthp = self.hp


class Armor:

   def __init__(self, name, desc, hardness, weight):
      self.name = name
      self.description = desc
      self.hardness = hardness
      self.weight = weight

class Weapon:

   def __init__(self, name, desc, damageRoll, weight):
      self.name = name
      self.description = desc
      self.damageRoll = damageRoll
      self.weight = weight
  
class Item:

   def __init__(self, name, desc, weight):
        self.name = name
        self.description = desc
        self.weight = weight

class Room(object):

    def __init__(self, name, desc):
        self.description = desc
        self.name = name
        self.up = None
        self.down = None
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.items = []
        self.monsters = []
        self.monsterChance = 2

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def printItems(self):
        if (len(self.items) > 0):
            print('There is a:')
            for i in range(len(self.items)):
                item = self.items[i]
                print(item.name)

    def getItems(self):
       return self.items

    def addMonster(self, monster):
       self.monsters.append(monster)

    def getMonster(self):
       chance = random.randint(1, self.monsterChance)
       if chance == 1 and (len(self.monsters) > 0):
          monsterChoice = random.randint(0, len(self.monsters)-1)
          return self.monsters[monsterChoice]
       else:
          return None


character = Character(5, 5, 5, 5, 5, 5)

r1 = Room('r1', 'You are in a small cave, with a barely audible sound of rushing water \ncoming from above. A exit of crumbled stones lies east, \nand to your south is a crack large enough to squeeze through.')
r2 = Room('r2', 'This is a tiny cave room, which you must crawl through to not smack into \nthe ceiling. An exit of broken stone is west, and a hole in \nthe wall is to the south.')
r3 = Room('r3', 'The cave ceiling seems to go on infinitely. There is \na large crack to the north, and a big hole to your east')
r4 = Room('r4', 'A small waterfall flows into a shallow lake. To the north is a \ngiant hole in the cave wall, and there is another hole to your west.')
r5 = Room('r5', 'A clear lake lies calmly at the far end, with a small \nriver flowing from it down through a crack below you, changing into a crashing \nwaterfall. You can climb down through the crack under you. A rope also dangles from a small crack to the ceiling, where a tiny ray of light flows through.')
r6 = Room('win', 'you win!')

r1.east = r2
r1.south = r3

r2.west = r1
r2.south = r4

r3.north = r1
r3.east = r4

r4.north = r2
r4.west = r3
r4.up = r5

r5.down = r4
r5.up = r6

r6.down = r5

character.currentRoom = r1

plasticCup = Item('plastic cup', 'It is just a useless, empty cup.', 3)
shovel = Item('shovel','It has a wooden handle, and a curved metal end for shoveling.', 5)

r1.addItem(plasticCup)
r5.addItem(shovel)

chainmail = Armor('chainmail', 'Rings of steel attach to create a strong, sturdy armor.', 10, 10)
character.addItem(chainmail)
character.equipArmor(chainmail)

shortsword = Weapon('shortsword', 'A thin, short blade with a thick wooden handle.', 7, 7)
bite = Weapon('bite', 'A set of nasty-looking sharp teeth', 4, 0)
spear = Weapon('spear', 'A thin wooden pole with a sharp arrowhead at the tip', 4, 5)

character.addItem(shortsword)
character.equipWeapon(shortsword)

goblin = Monster([shovel, plasticCup], [100, 100], 1, 3, 7, bite, chainmail, 'goblin', 'An evil Goblin')
kobold = Monster([spear, plasticCup], [200, 100], 5, 3, 2, spear, chainmail, 'kobold', 'A mean-looking Kobold')
orc = Monster([shortsword, shovel], [200, 100], 3, 9, 6, shortsword, chainmail, 'orc', 'A crazy orc')

goblin.equipArmor(chainmail)
kobold.equipArmor(chainmail)
orc.equipArmor(chainmail)

r2.addMonster(goblin)
r4.addMonster(kobold)
r4.addMonster(orc)
r3.addMonster(orc)
r5.addMonster(orc)
r5.addMonster(kobold)


def attack(command):
   if 'attack' in command or 'hit' in command or 'kill' in command:
      if character.currentMonster != None and character.currentMonster.name in command:
         character.attack()
         if character.currentMonster.checkForDeath():
            return True
         character.currentMonster.attack()
         character.checkForDeath()
      else:
         print('That is not in this room.')
      return True

def unequip(command):  
   if 'unequip' in command:
       found = False
       currentInventory = character.getItems()
       for i in (currentInventory):
          if i.name in command:
             if ((character.weapon != None) and (character.weapon.name == i.name)):
                print('You unequip the ' + i.name)
                found = True
                character.weapon = None
             elif ((character.armor != None) and (character.armor.name == i.name)):
                print('You unequip the ' + i.name)
                found = True
                character.armor = None
                character.ac = 0
       if not found:
          print('You do not have that in your inventory.')
       return True

def equip(command):
   if 'equip' in command:
       found = False
       currentInventory = character.getItems()
       for i in (currentInventory):
          if i.name in command:
             if isinstance(i, Weapon):
                print('You equip the ' + i.name)
                found = True
                character.weapon = i
             elif isinstance(i, Armor):
                print('You equip the ' + i.name)
                found = True
                character.armor = i
                character.ac = i.hardness
             elif isinstance(i, Item):
                print('That is not something you can equip.')
                found = True
       if not found:
          print('You do not have that in your inventory.')
       return True

def displayStats(command):
   if 'stat' in command:
      print('Strength: ' + str(character.strength))
      print('Dexterity: ' + str(character.dexterity))
      print('Constitution: ' + str(character.constitution))
      print('Intelligence: ' + str(character.intelligence))
      print('Stamina: ' + str(character.stamina))
      print('Luck: ' + str(character.luck))
      print('HP: ' + str(character.currenthp) + '/' + str(character.hp))
      print('Carrying Capacity: ' + str(character.currentcc) + '/' + str(character.cc))
      if character.weapon:
         print('Attack:')
         print(character.weapon.name + ' +' + str(character.dexterity) + ' d' + str(character.weapon.damageRoll) + '+' + str(character.strength))
      print('AC: ' + str(character.ac))
      return True

def dropItem(command):
   if 'drop' in command:
       found = False
       currentInventory = character.getItems()
       for i in (currentInventory):
          if i.name in " ".join(command):
             print('You drop the ' + i.name + ' on the floor.')
             character.removeItem(i)
             character.currentRoom.addItem(i)
             found = True
             currentcc = character.calculateWeight()
             character.currentcc = currentcc
       if not found:
          print('You do not have that in your inventory.')
       return True  

def takeItem(command):
   if 'take' == command[0] or 'get' == command[0] or 'pick' == command[0]:
       found = False
       currentRoomItems = character.currentRoom.getItems()
       for i in (currentRoomItems):
          if i.name in " ".join(command):
             if character.currentcc + i.weight > character.cc:
                print('That is too heavy for you!')
                return True
             print('You add the ' + i.name + ' to your inventory')
             character.addItem(i)
             character.currentRoom.removeItem(i)
             found = True
             character.currentcc = character.calculateWeight()
       if not found:
           if (character.currentMonster):
             if character.currentMonster.name.lower() in command:
                print('That\'s not going to happen.')
                found = True
       if not found:
           print('That is not in this room.')
       return True
   if (('take' == command[0]) or ('get' == command[0])) and ('all' == command[1]):
      for i in (currentRoomItems):
            if character.currentcc + i.weight > character.cc:
               print('The ' + i.name + ' is to heavy for you!')
               return True
            print('You add the ' + i.name + ' to your inventory')
            character.addItem(i)
            character.currentRoom.removeItem(i)
            character.currentcc = currentcc

def checkMonster():
   monster = character.currentRoom.getMonster()
   character.setMonster(monster)
   if character.currentMonster:
      exits = []
      if character.currentRoom.up:
         exits.append('up')
      if character.currentRoom.down:
         exits.append('down')
      if character.currentRoom.south:
         exits.append('south')
      if character.currentRoom.north:
         exits.append('north')
      if character.currentRoom.east:
         exits.append('east')
      if character.currentRoom.west:
         exits.append('west')
      exitsLen = random.randint(0, len(exits)-1)
      character.currentMonster.blocked = exits[exitsLen] 
   
      
def move(command):
    if 'north' in command:
        if character.currentRoom.north:
           if character.currentMonster:
              if character.currentMonster.blocked != 'north':
                  character.currentRoom = character.currentRoom.north
                  checkMonster()
                  return True
              else:
                  print('The way is blocked.')
           else:
              character.currentRoom = character.currentRoom.north
              checkMonster()
              return True
        else:
            print('You cannot go that way!')
        return True
    if 'east' in command:
        if character.currentRoom.east:
           if character.currentMonster:
               if character.currentMonster.blocked != 'east':
                  character.currentRoom = character.currentRoom.east
                  checkMonster()
                  return True
               else:
                  print('The way is blocked.')
           else:
              character.currentRoom = character.currentRoom.east
              checkMonster()
              return True
        else:
            print('You cannot go that way!')
        return True
    if 'south' in command:
        if character.currentRoom.south:
           if character.currentMonster:
              if character.currentMonster.blocked != 'south':
                  character.currentRoom = character.currentRoom.south
                  checkMonster()
                  return True
              else:
                  print('The way is blocked.')
           else:
              character.currentRoom = character.currentRoom.south
              checkMonster()
              return True
        else:
            print('You cannot go that way!')
        return True
    if 'west' in command:
        if character.currentRoom.west:
           if character.currentMonster:
              if character.currentMonster.blocked != 'west':
                  character.currentRoom = character.currentRoom.west
                  checkMonster()
                  return True
              else:
                  print('The way is blocked.')
           else:
              character.currentRoom = character.currentRoom.west
              checkMonster()
              return True
        else:
            print('You cannot go that way!')
        return True
    if 'up' in command:
        if character.currentRoom.up:
           if character.currentMonster:
              if character.currentMonster.blocked != 'up':
                  character.currentRoom = character.currentRoom.up
                  checkMonster()
                  return True
              else:
                  print('The way is blocked.')
           else:
              character.currentRoom = character.currentRoom.up
              checkMonster()
              return True
        else:
            print('You cannot go that way!')
        return True
    if 'down' in command:
         if character.currentRoom.down:
           if character.currentMonster:
              if character.currentMonster.blocked != 'down':
                  character.currentRoom = character.currentRoom.down
                  checkMonster()
                  return True
              else:
                  print('The way is blocked.')
           else:
              character.currentRoom = character.currentRoom.down
              checkMonster()
              return True
         else:
            print('You cannot go that way!')
         return True

def examine(command):
   if 'examine' == command[0]:
       found = False
       currentRoomItems = character.currentRoom.getItems()
       for i in (currentRoomItems):
          if i.name in command:
             print(i.description)
             found = True
       if not found:
          for i in (character.getItems()):
             if i.name in " ".join(command):
                print(i.description)
                found = True
       if not found:
          if (character.currentMonster):
             if character.currentMonster.name.lower() in command:
                print(character.currentMonster.description)
                found = True
       if not found:
          print('That is not in this room.')
       return True

def terminate(command):
    if 'exit' in command or 'quit' in command:
        print('goodbye!')
        sys.exit()

def viewInventory(command):
   if 'inventory' in command or ('i' == command[0]):
       character.printItems()
       return True

def printStatus():
    print()
    print(character.currentRoom.name)
    print(character.currentRoom.description)
    character.currentRoom.printItems()
    character.printMonster()
    print()

def getCommand():
    print('What do you do?')
    command = input()
    return command.lower().split()

character.currentcc = character.calculateWeight()

while True:

    printStatus()
    command = getCommand()
    
    if 'look' in command:
        continue

    if attack(command):
       continue

    if unequip(command): 
       continue

    if equip(command):
       continue

    if displayStats(command):
       continue

    if terminate(command):
       continue

    if viewInventory(command):
       continue

    if examine(command):
       continue

    if takeItem(command):
       continue
      
    if move(command):
       continue

    if dropItem(command):
       continue
      
    print('Please type in a valid command')
