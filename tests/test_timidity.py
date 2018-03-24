
import unittest
import os
from timidity.player import Timidity

class TestTimidity(unittest.TestCase):

    def setUp(self):
        self.player = Timidity(os.path.join(os.path.dirname(__file__), "MIDI_sample.mid"))

    def test_commands(self):
        self.player.toggle_pause()
        self.player.key_up()
        self.player.toggle_pause()
        self.player.quit()
