# Паттерн Абстрактная фабрика
class GUIFactory: # Абстрактный класс GUI фабрики
    def create_button(self):
        pass
        
    def create_checkbox(self):
        pass
        
class WinFactory(GUIFactory): 
    def create_button(self):
        return WinButton()
    
    def create_checkbox(self):
        return WinCheckbox()
        
class MacFactory(GUIFactory): 
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()
        
class Button:
    def paint(self):
        pass
        
class Checkbox:
    def paint(self):
        pass
        
class WinButton(Button): 
    def paint(self):
        return 'Рисование кнопки выигрыша'
    
class MacButton(Button):
    def paint(self):
        return 'Рисование кнопки Mac'
        
class WinCheckbox(Checkbox):
     def paint(self):
        return 'Устанавливаем флажок "Выиграть"'
    
class MacCheckbox(Checkbox):
    def paint(self):
        return 'Рисование флажка Mac'
