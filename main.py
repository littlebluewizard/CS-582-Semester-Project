import arcade
import arcade.gui
import random

# Constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Speech Pong"
PRIMARY_BACK_GROUND_COLOR = (202, 199, 183)
DARK_MODE_COLOR = (18, 18, 18)

# Placeholder Variables
back_ground_color = (202, 199, 183)

# Start Menu Button Style:
primary_button_style = {
    "bg_color": (77, 94, 114),
    "bg_color_pressed": (63, 106, 138),
    "font_color": arcade.color.WHITE,
    "font_color_pressed": arcade.color.WHITE
}


class MenuView(arcade.View):
    def set_mouse_platform_visible(self, platform_visible=None):
        pass

    def setup(self):
        pass

    def __init__(self):
        super().__init__()

        # UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set the background color
        arcade.set_background_color(back_ground_color)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Title
        title_text_label = arcade.gui.UILabel(text="Speech Pong", width=250, height=50,
                                              text_color=(77, 94, 114), bold=True, font_size=25,
                                              align="center")
        self.v_box.add(title_text_label.with_space_around(bottom=10))

        desc_text_label = arcade.gui.UILabel(text="Dylan James, Ernesto Lacanlale, James Ardilla, Thomas Bellegarde",
                                             width=500, height=50, text_color=(77, 94, 114),
                                             bold=True, font_size=10, align="center")
        self.v_box.add(desc_text_label.with_space_around(bottom=20))

        # Menu buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style=primary_button_style)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200, style=primary_button_style)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200, style=primary_button_style)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        @start_button.event("on_click")
        def on_click_start(event):
            if event:
                game_view = GameView()
                game_view.setup()
                self.window.show_view(game_view)

        @settings_button.event("on_click")
        def on_click_settings(event):
            if event:
                settings_view = SettingView()
                settings_view.setup()
                self.window.show_view(settings_view)

        @quit_button.event("on_click")
        def on_click_exit(event):
            if event:
                arcade.exit()

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_show(self):
        """ Called when switching to this view"""
        pass

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # UI manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Background color
        global back_ground_color
        arcade.set_background_color(back_ground_color)

        # Back Button
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=200, style=primary_button_style)

        # Layouts, one horizontal, two vertical to split the screen.
        self.h_box = arcade.gui.UIBoxLayout(vertical=False)
        self.v_box_left = arcade.gui.UIBoxLayout()
        self.v_box_right = arcade.gui.UIBoxLayout()

        # Left Side (Player 1)
        self.player1_title = arcade.gui.UILabel(text="Player 1",
                                                width=200, height=50, text_color=(77, 94, 114),
                                                bold=True, font_size=20, align="center", font_name="Arrakis")
        self.player1_move = arcade.gui.UILabel(text="Latest Move:",
                                               width=200, height=50, text_color=(77, 94, 114),
                                               bold=True, font_size=13, align="center")
        self.player1_move_count = arcade.gui.UILabel(text="Move Count:",
                                                     width=200, height=50, text_color=(77, 94, 114),
                                                     bold=True, font_size=13, align="center")
        self.player1_move_text = arcade.gui.UILabel(text="",
                                                    width=50, height=50, text_color=(77, 94, 114),
                                                    bold=True, font_size=13, align="center")
        self.player1_move_count_num = arcade.gui.UILabel(text="0",
                                                         width=100, height=50, text_color=(77, 94, 114),
                                                         bold=True, font_size=13, align="center")

        self.v_box_left.add(self.player1_title)
        self.v_box_left.add(self.player1_move)
        self.v_box_left.add(self.player1_move_count)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_x=-100,
                child=self.player1_move_text
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_x=-130,
                align_y=-50,
                child=self.player1_move_count_num
            )
        )

        # Right Side (Player 2)
        self.player2_title = arcade.gui.UILabel(text="Player 2",
                                                width=200, height=50, text_color=(77, 94, 114),
                                                bold=True, font_size=20, align="center", font_name="Arrakis")
        self.player2_move = arcade.gui.UILabel(text="Latest Move:",
                                               width=200, height=50, text_color=(77, 94, 114),
                                               bold=True, font_size=13, align="center")
        self.player2_move_count = arcade.gui.UILabel(text="Move Count:",
                                                     width=200, height=50, text_color=(77, 94, 114),
                                                     bold=True, font_size=13, align="center")
        self.player2_move_text = arcade.gui.UILabel(text="",
                                                    width=50, height=50, text_color=(77, 94, 114),
                                                    bold=True, font_size=13, align="center")
        self.player2_move_count_num = arcade.gui.UILabel(text="0",
                                                         width=50, height=50, text_color=(77, 94, 114),
                                                         bold=True, font_size=13, align="center")
        self.v_box_right.add(self.player2_title)
        self.v_box_right.add(self.player2_move)
        self.v_box_right.add(self.player2_move_count)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_x=300,
                child=self.player2_move_text
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_x=270,
                align_y=-50,
                child=self.player2_move_count_num
            )
        )

        self.h_box.add(self.v_box_left.with_space_around(right=100))
        self.h_box.add(self.v_box_right.with_space_around(left=100))

        @self.back_button.event("on_click")
        def on_click_back(event):
            if event:
                menu_view = MenuView()
                menu_view.setup()
                self.window.show_view(menu_view)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.h_box)
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                align_x=20,
                align_y=-10,
                child=self.back_button)
        )

    def setup(self):
        self.clear()
        pass

    def on_show(self):
        """ Called when switching to this view"""
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_line(start_x=460, start_y=0, end_x=460, end_y=600, color=arcade.color.WHITE)
        self.manager.draw()

    def set_latest_move(self, player, move):
        """
        Updates the latest move for target player.

        :param string player: "player1" or "player2"
        :param string move: Any string or "Up" / "Down"
        """
        if player == "player1":
            self.player1_move_text.text = move
        elif player == "player2":
            self.player2_move_text.text = move

    def inc_move_counter(self, player):
        """
        Increments the move counter for target player.

        :param string player: "player1" or "player2"
        """
        if player == "player1":
            self.player1_move_count_num.text = str(int(self.player1_move_count_num.text) + 1)
        elif player == "player2":
            self.player2_move_count_num.text = str(int(self.player1_move_count_num.text) + 1)

    def clear_move_counter(self, player):
        """
        Clears the move counter for target player.

        :param string player: "player1" or "player2"
        """
        if player == "player1":
            self.player1_move_count_num.text = 0
        elif player == "player2":
            self.player2_move_count_num.text = 0

    def get_move_counter(self, player):
        """
        Returns the move counter for target player.

        :return int:
        """
        if player == "player1":
            return int(self.player1_move_count_num.text)
        elif player == "player2":
            return int(self.player2_move_count_num.text)

    # I use this to test, use T for counters, and Y for latest move.
    def on_key_press(self, key, _modifiers):
        if key == 116:
            self.inc_move_counter("player2")
            self.inc_move_counter("player1")
        if key == 121:
            moves = ["Up", "Down"]
            self.set_latest_move("player1", moves[random.randint(0, 1)])
            self.set_latest_move("player2", moves[random.randint(0, 1)])

    def on_hide_view(self):
        self.manager.disable()


class SettingView(arcade.View):
    def __init__(self):
        super().__init__()

        # UI manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        global back_ground_color
        # Background color
        arcade.set_background_color(back_ground_color)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        self.dark_mode = False
        self.dark_mode_button = arcade.gui.UIFlatButton(text="Enable Dark Mode", width=150, style=primary_button_style)
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=150, style=primary_button_style)
        self.v_box.add(self.dark_mode_button)
        self.v_box.add(self.back_button.with_space_around(top=20))

        global DARK_MODE_COLOR
        if back_ground_color == DARK_MODE_COLOR:
            self.dark_mode = True
            self.dark_mode_button.text = "Disable Dark Mode"

        @self.dark_mode_button.event("on_click")
        def on_click_dark_mode(event):
            if event:
                global back_ground_color
                global DARK_MODE_COLOR
                if not self.dark_mode:
                    self.dark_mode = True
                    self.dark_mode_button.text = "Disable Dark Mode"
                    back_ground_color = DARK_MODE_COLOR
                    arcade.set_background_color(DARK_MODE_COLOR)
                else:
                    self.dark_mode = False
                    self.dark_mode_button.text = "Enable Dark Mode"
                    arcade.set_background_color(PRIMARY_BACK_GROUND_COLOR)
                    back_ground_color = PRIMARY_BACK_GROUND_COLOR

        @self.back_button.event("on_click")
        def on_click_back(event):
            if event:
                menu_view = MenuView()
                menu_view.setup()
                self.window.show_view(menu_view)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def setup(self):
        pass

    def on_show(self):
        """ Called when switching to this view"""
        pass

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)

    # game_stats = GameView()
    # Here are some function examples:
    # game_stats.inc_move_counter("player1")
    # game_stats.clear_move_counter("player1")
    # game_stats.get_move_counter("player1")
    # game_stats.set_latest_move("player1", "Up")

    arcade.run()  # Anything after this will not run, unless we multi-thread


if __name__ == "__main__":
    main()
