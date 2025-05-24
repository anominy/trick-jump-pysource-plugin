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

from typing import Final
from messages import SayText2
from commands.typed import TypedSayCommand, TypedClientCommand, CommandInfo
from players.entity import Player
from commands import CommandReturn

import random


@TypedSayCommand('!roll')
@TypedSayCommand('/roll')
@TypedClientCommand('sm_roll')
@TypedClientCommand('sp_roll')
def on_roll_cmd(info: CommandInfo) -> CommandReturn:
    player: Final[Player] = Player(info.index)
    player_name: Final[str] = player.get_name()

    roll: Final[int] = random.randint(0, 100)
    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 rolled \x05' + str(roll) + '\x08!') \
        .send()

    return CommandReturn.BLOCK
