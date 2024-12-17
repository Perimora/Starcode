from typing import List

from IPython.core.display_functions import display, clear_output
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


class HangmanGui:

    def __init__(self, masked_target: List, player_error_count: int = 0):
        # initial member creation
        self.fig, self.ax = plt.subplots()
        self.masked_target = masked_target
        self.player_error_count = player_error_count
        self.covered_letters = {}

        # define mapping for error counts and drawing functions
        self.error_steps = [
            self.draw_base,
            self.draw_pillar,
            self.draw_beam,
            self.draw_rope,
            self.draw_head,
            self.draw_body,
            self.draw_left_arm,
            self.draw_right_arm,
            self.draw_left_leg,
            self.draw_right_leg
        ]

        # plot initial game state
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 5)
        self.ax.axis('off')
        self.ax.set_aspect('equal')

        self.display()

    def update(self, masked_target: List, player_error_count: int, letters: List[str]):
        self.masked_target = masked_target
        self.player_error_count = player_error_count
        self.covered_letters = set(letters)

    def display(self):
        # reset plot
        self.ax.cla()

        self.ax.axis('off')
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 5)
        self.ax.axis('off')
        self.ax.set_aspect('equal')
        # show masked target
        self.display_masked_word()

        # draw hangman figure for given error count
        for i in range(self.player_error_count):
            self.error_steps[i]()

        clear_output(wait=True)
        display(self.fig)

    def cycle(self, masked_target: List, player_error_count: int, letters: List[str]):
        self.update(masked_target, player_error_count, letters)
        self.display()

    def display_masked_word(self):
        masked_word = " ".join(self.masked_target)
        self.ax.text(2.5, 2.5, masked_word, fontsize=20, ha='left', va='center')
        guessed_letters = ", ".join(sorted(self.covered_letters))
        self.ax.text(2.5, 1.75, f"Guessed letters: {guessed_letters}", fontsize=12, ha='left', va='center')

    def draw_base(self):
        self.ax.add_line(Line2D([-1, 1], [-2, -2], linewidth=3, color='black'))

    def draw_pillar(self):
        self.ax.add_line(Line2D([0, 0], [-2, 4], linewidth=3, color='black'))

    def draw_beam(self):
        self.ax.add_line(Line2D([0, 1], [4, 4], linewidth=3, color='black'))

    def draw_rope(self):
        self.ax.add_line(Line2D([1, 1], [4, 3.5], linewidth=3, color='black'))

    def draw_head(self):
        self.ax.add_patch(Circle((1, 3.2), 0.3, fill=False, color='black', linewidth=3))

    def draw_body(self):
        self.ax.add_line(Line2D([1, 1], [2.9, 2], linewidth=3, color='black'))

    def draw_left_arm(self):
        self.ax.add_line(Line2D([1, 0.5], [2.8, 2.5], linewidth=3, color='black'))

    def draw_right_arm(self):
        self.ax.add_line(Line2D([1, 1.5], [2.8, 2.5], linewidth=3, color='black'))

    def draw_left_leg(self):
        self.ax.add_line(Line2D([1, 0.7], [2, 1.5], linewidth=3, color='black'))

    def draw_right_leg(self):
        self.ax.add_line(Line2D([1, 1.3], [2, 1.5], linewidth=3, color='black'))
