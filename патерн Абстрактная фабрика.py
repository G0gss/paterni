class Director: # Класс Director, который использует объект Builder для построения объекта
    def init(self): # задаем значение `None` для переменной `builder`, когда создается новый объект `Director`.
        self.builder = None
        
    def set_builder(self, builder): # устанавливаем значение переменной `builder` в объект `Builder`.
        self.builder = builder
        
    def construct_building(self): 
        self.builder.new_building() # Создаём новый объект в `Builder`
        self.builder.build_floor() # Создаём пол для объекта в `Builder`
        self.builder.build_walls # Создаём стены для объекта в `Builder`