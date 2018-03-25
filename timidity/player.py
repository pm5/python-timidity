#!/usr/bin/env python

import subprocess

class Timidity(object):

    def __init__(self, filename, *args):
        self.filename = filename
        self.args = args
        command = ["timidity", "-in"]
        command.extend(args)
        command.append(filename)
        self._proc = subprocess.Popen(command,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)

_single_key_commands = [
          ["skip_back", b"b"],
          ["skip_foward", b"f"],
          ["volume_up", b"V"],
          ["volume_down", b"v"],
          ["restar_file", b"r"],
          ["quit", b"q"],
          ["toggle_pause", b"s"],
          ["key_up", b"+"],
          ["key_down", b"-"],
          ["speed_up", b">"],
          ["speed_down", b"<"],
        ]

def make_single_key_command(name, key):
    def method(self):
        self._proc.stdin.write(key)
        self._proc.stdin.flush()
    method.__name__ = name
    return method

for cmd in _single_key_commands:
    name = cmd[0]
    key = cmd[1]
    setattr(Timidity, name, make_single_key_command(name, key))
