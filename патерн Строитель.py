class Director: 
        self.builder = None
        
    def set_builder(self, builder): 
        self.builder = builder
        
    def construct_building(self): 
        self.builder.new_building() 
        self.builder.build_floor() 
        self.builder.build_walls 
