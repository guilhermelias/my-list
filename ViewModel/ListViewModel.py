class ListViewModel:

    def __init__(self, list):
        self._name = list.name
        self._item = list.item
        self._value = list.value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, item):
        self._item = item
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value