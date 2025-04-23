from Container.imports_library import *

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.play = False
        self._create()
   
    def _create(self):
        """Create the menu structure and add buttons"""
        self.main_menu = pygame_menu.Menu('Welcome', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.load_game_screen = pygame_menu.Menu('Load Game', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.settings_screen = pygame_menu.Menu('Settings', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        
        # Add buttons to main menu
        self.main_menu.add.button('Play', self._play)
        self.main_menu.add.button('Load Game', self._load_game)
        self.main_menu.add.button('Settings', self._settings)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)
   
    def _play(self):
        """Handle play button action"""
        self.play = True
   
    def _load_game(self):
        """Show load game screen with saved games"""
        self.load_game_screen.clear()
        saved_games = [
            "Save Game 1",
            "Save Game 2",
            "Save Game 3"
        ]
        
        for index, save in enumerate(saved_games):
            self.load_game_screen.add.button(save, lambda i=index: self.load_saved_game(i))
            
        self.load_game_screen.add.button('Return to Main Menu', pygame_menu.events.BACK)
        self.main_menu._open(self.load_game_screen)
    
    def load_saved_game(self, index):
        """Load a specific saved game"""
        print(f"Loading saved game at index {index}")
        self.play = True
        
    def _settings(self):
        """Show settings screen with sliders"""
        self.settings_screen.clear()
        self.music_volume = self.settings_screen.add.range_slider('Music Volume', default=50, range_values=(0, 100), increment=1)
        self.sfx_volume = self.settings_screen.add.range_slider('Sound Effects', default=50, range_values=(0, 100), increment=1)
        self.frame_rate = self.settings_screen.add.range_slider('Frame Rate', default=60, range_values=(30, 120), increment=1)
        self.brightness = self.settings_screen.add.range_slider('Brightness', default=100, range_values=(0, 100), increment=1)
        self.settings_screen.add.button('Return to Main Menu', pygame_menu.events.BACK)
        self.main_menu._open(self.settings_screen)

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.play = True
        self.restart_game = False
        self.exit_game_varible = False
        self._create()
   
    def _create(self):
        """Create pause menu structure and add buttons"""
        self.pause_menu = pygame_menu.Menu('Pause Menu', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        self.settings_screen = pygame_menu.Menu('Settings', self.width, self.height, theme=pygame_menu.themes.THEME_DARK)
        
        # Add buttons to pause menu
        self.pause_menu.add.button('Resume', self._resume)
        self.pause_menu.add.button('Restart', self._restart)
        self.pause_menu.add.button('Settings', self._settings)
        self.pause_menu.add.button('Exit', self._exit_game)
   
    def _resume(self):
        """Resume the game"""
        self.play = True
   
    def _restart(self):
        """Restart the game"""
        self.restart_game = True
        self.play = True
   
    def _settings(self):
        """Show settings screen with sliders"""
        self.settings_screen.clear()
        self.music_volume = self.settings_screen.add.range_slider('Music Volume', default=50, range_values=(0, 100), increment=1)
        self.sfx_volume = self.settings_screen.add.range_slider('Sound Effects', default=50, range_values=(0, 100), increment=1)
        self.frame_rate = self.settings_screen.add.range_slider('Frame Rate', default=60, range_values=(30, 120), increment=1)
        self.brightness = self.settings_screen.add.range_slider('Brightness', default=100, range_values=(0, 100), increment=1)
        self.settings_screen.add.button('Return to Pause Menu', pygame_menu.events.BACK)
        self.pause_menu._open(self.settings_screen)
   
    def _exit_game(self):
        """Exit the game"""
        self.exit_game_varible = True
        self.play = False
