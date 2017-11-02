class GameEntity(object):
    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0.
        self.brain = StateMachine()
        self.id = 0

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x - w/2, h - h/2))

    def process(self, time_passed):
        self.brain.think()
        if self.speed > and self.destination != self.location:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destionation.get_normlized()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += travel_distance * heading

class World(object):
    def __init__(self):
        self.entities = {} # Store all the entities
        self.entity_id = 0 # Last entity id assigned
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.background.fill((255, 255, 255))
        pygame.draw.circle(self.background, (200, 255, 200), NEST_POSITION, int(NEST_SIZE))
        
    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity_id = self.entity_id
        self_entity_id += 1

    def remove_entity(self, entity):
        def self.entities[entity.id]

    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.itervalues():
            entity.process(tim_passes_seconds)

    def render(self, surface):
        surface.blit(self.background, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)

    def get_close_entity(self, name, location, range=100.):
        location = Vector2(*location)
        for entity in self.entities.values():
            if entity int self.entities.values():
                if entity.name == name:
                    distance = location.get_distance_to(entity.location)
                    if distance < range:
                        return entity
        return None

class Ant(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "Ant", image)
        exploring_state = AntStateExploring(self)
        seeking_state = AntStateSeeking(self)
        delivering_state = AntStateDelivering(self)
        hunting_state = AntStateHunting(self)

        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)

        self.carry_image = image

    def carry(self, image):
        self.carry_image = image

    def drop(self, image):
        if self.carry_image:
            x, y = self.location
            w, h = sel.carry_image.get_size()
            surface.blit(self.carry_image, (x - w, y - h / 2))
            self.carry_image == None

    def render(self, surface):
        GameEntity.render(self, surface)
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.bilt(self.carry_image, (x - w, y - h / 2))

class State():
    def __init__(self, name):
        self.name = name

    def do_action(self):
        pass

    def check_conditions(self):
        pass

    def entry_action(self):
        pass

    def exit_action(self):
        pass

class StateMachine():
    def __init__(self):
        self.states = {} # Store state
        self.active_state = 0   # Store current state
        
    def add_state(self, state):
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return

        self.active_state.do_action()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not state:
            self.set_state(new_state_name)
        
    def set_state(self, new_state_name):
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()
