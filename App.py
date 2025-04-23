from Container.imports_library import *
import Menus, Map

# main
class Application:
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screenWidth, self.screenHeight = 700, 700
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.middle_pressed = False
        self.change_map = False
        self.x, self.y = 0, 0 
        pygame.display.set_caption("App")
        self.menus()
        self.map_size = (10,10)
        self.map_manager = Map.Ground(screen_size=self.screen.get_size(), cell_size=self.map_size, active_color=pygame.Color("Red"))
        self.x, self.y = 0, 0 
        self.map_manager.move_camera(self.x, self.y)

    def on_resize(self) -> None:
        window_size = self.screen.get_size()
        new_w, new_h = window_size[0], window_size[1]
        # main menu
        self.Main_Menu.main_menu.resize(new_w, new_h)
        self.Main_Menu.load_game_screen.resize(new_w, new_h)
        self.Main_Menu.settings_screen.resize(new_w, new_h)

        self.Pause_Menu.pause_menu.resize(new_w, new_h)
        self.Pause_Menu.settings_screen.resize(new_w, new_h)

    def menus(self):
        self.Main_Menu = Menus.MainMenu(self.screen)
        self.Pause_Menu = Menus.PauseMenu(self.screen)
        
    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.map_manager.update_screen_size((event.w, event.h))
                    self.on_resize()
                # menu
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_p) and self.Main_Menu.play:
                        self.Pause_Menu.play = not(self.Pause_Menu.play)
                if self.Main_Menu.play and not self.change_map:
                    self.map_manager = Map.Ground(screen_size=self.screen.get_size(), cell_size=self.map_size, active_color=pygame.Color("Red"))
                    self.x, self.y = 0, 0 
                    self.map_manager.move_camera(self.x, self.y)
                    self.change_map = True
                # move map
                if self.Main_Menu.play and self.Pause_Menu.play:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 2:
                            self.middle_pressed = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 2:
                            self.middle_pressed = False
                            self.x, self.y = event.pos
                    elif event.type == pygame.MOUSEMOTION:
                        if self.middle_pressed:
                            self.map_manager.move_camera(self.x,self.y)
                    self.map_manager.handle_event(event)
            self.screen.fill(pygame.Color("black"))
            # map
            if self.Main_Menu.play and self.Pause_Menu.play:
                self.map_manager.draw(screen=self.screen)
            # menu update
            if (not self.Main_Menu.play) or self.Pause_Menu.exit_game_varible:
                self.Main_Menu.main_menu.update(events)
                self.Main_Menu.main_menu.draw(self.screen)
            elif self.Main_Menu.play and (not self.Pause_Menu.play):
                self.Pause_Menu.pause_menu.update(events)
                self.Pause_Menu.pause_menu.draw(self.screen)
            if self.Pause_Menu.exit_game_varible:
                self.Main_Menu.play = False
                self.Pause_Menu.exit_game_varible = False
                self.Pause_Menu.play = True
                self.Pause_Menu.restart_game = False
                self.change_map = False
            # This is to update the scene
            self.clock.tick(64)
            pygame.display.flip()
            pygame.display.update()

# loop
if __name__ == "__main__":
    application = Application()
    application.run()
