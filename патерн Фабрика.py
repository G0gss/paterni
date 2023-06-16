# Паттерн Абстрактная фабрика
class GUIFactory: # Абстрактный класс GUI фабрики
    def create_button(self):
        pass
        
    def create_checkbox(self):
        pass
        
class WinFactory(GUIFactory): # Конкретная Win фабрика, которая создает Win кнопки и чекбоксы
    def create_button(self):
        return WinButton()
    
    def create_checkbox(self):
        return WinCheckbox()
        
class MacFactory(GUIFactory): # Конкретная Mac фабрика, которая создает Mac кнопки и чекбоксы
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()
        
class Button: # Абстрактный класс для кнопок
    def paint(self):
        pass
        
class Checkbox: # Абстрактный класс для чекбоксов
    def paint(self):
        pass
        
class WinButton(Button): # Класс для создания Win кнопок
    def paint(self):
        return 'Рисование кнопки выигрыша'
    
class MacButton(Button): # Класс для создания Mac кнопок
    def paint(self):
        return 'Рисование кнопки Mac'
        
class WinCheckbox(Checkbox): # Класс для создания Win чекбоксов
     def paint(self):
        return 'Устанавливаем флажок "Выиграть"'
    
class MacCheckbox(Checkbox): # Класс для создания Mac чекбоксов
    def paint(self):
        return 'Рисование флажка Mac'