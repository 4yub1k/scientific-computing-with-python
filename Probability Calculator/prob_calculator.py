import copy
import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs):
        self.contents = list(Counter(kwargs).elements())
        self.contents_copy = copy.copy(self.contents)

    def draw(self, num_balls):
        self.contents = copy.copy(self.contents_copy)  # Restore list

        if num_balls > len(self.contents):
            return self.contents
        """Draw "num_balls" number of balls from contents,
            same like of pop (remove and return the item)
        """
        self.drawn_balls = [
            self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls)
        ]
        return self.drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    balls_present = 0
    for _ in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)

        """Check if Balls in exected are present in Balls drawn,
            Expected balls can be greater but not less in drawn balls.
        """
        if all(
            list(map(lambda ball: drawn.count(ball[0]) >= ball[1], expected_balls.items()))
        ):
            balls_present += 1

    return balls_present / num_experiments  # n/m
