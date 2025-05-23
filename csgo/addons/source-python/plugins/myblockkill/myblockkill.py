#  Trick Jump Sp Plugin
#
#  Copyright (C) 2025  anominy
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Any
from messages import SayText2
from commands.server import ServerCommand
from commands import CommandReturn


def load() -> None:
    SayText2('\x03>^< \x08| The \x09myblockkill\x08 plugin is loaded!') \
        .send()


def unload() -> None:
    SayText2('\x03>^< \x08| The \x09myblockkill\x08 plugin is unloaded!') \
        .send()


@ServerCommand('kill')
def on_kill_cmd(command: Any) -> CommandReturn:
    return CommandReturn.BLOCK
