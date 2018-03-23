#!/usr/bin/env python

import subprocess


class Timidity:

    def __init__(self, filename, *args):
        self.filename = filename
        self.args = args
        self._proc = subprocess.Popen(["timidity", "-in", *args, filename],
                                      stdin=subprocess.PIPE)

    def pause(self):
        self._proc.stdin.write("s")

    def play(self):
        self._proc.stdin.write("s")
