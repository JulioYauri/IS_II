# -*- coding: utf-8 -*-
class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
        

class Creator(object): 
    def create(self, name, sell_in, quality): 
        if name == "Aged Brie": 
            return Brie(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros": 
            return Sulfuras(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert": 
            return Backstage(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)

class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self): 
        self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0 and self.quality > 0: 
            self.quality = self.quality - 1
    
class Brie(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0 and self.quality < 50: 
            self.quality = self.quality + 1

class Sulfuras(Item):
    def update_quality(self):
        # si se verifica la funcion update_quality antes del 
        # refactoring, ningún atributo del item se modifica
        # cuando el item.name es "Sulfuras ..."
        pass 


class Backstage(Item):
    def update_quality(self):
        if self.quality < 50: 
            self.quality = self.quality + 1
            if self.sell_in < 11 and self.quality < 50: 
                self.quality = self.quality + 1
            if self.sell_in < 6 and self.quality < 50: 
                self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0: 
            self.quality = 0