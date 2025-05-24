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
from events import Event, GameEvent
from messages import SayText2
from players.entity import Player
from commands.typed import TypedSayCommand, TypedClientCommand, CommandInfo
from commands import CommandReturn


@Event('player_spawn')
def on_player_spawn(event: GameEvent) -> None:
    player: Final[Player] = Player.from_userid(int(event['userid']))
    player.set_noblock(True)


@TypedSayCommand('!noblock')
@TypedSayCommand('/noblock')
@TypedClientCommand('sm_noblock')
@TypedClientCommand('sp_noblock')
@TypedSayCommand('!block')
@TypedSayCommand('/block')
@TypedClientCommand('sm_block')
@TypedClientCommand('sp_block')
def on_no_block_cmd(info: CommandInfo) -> CommandReturn:
    player: Final[Player] = Player(info.index)
    player_name: Final[str] = player.name
    player_block: Final[bool] = not player.get_noblock()

    player.set_noblock(player_block)
    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 is ' \
             + ('enabled' if player_block else 'disabled') \
             + ' \x05no block\x08!') \
        .send()

    return CommandReturn.BLOCK
