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
from entities.entity import Entity
from commands.typed import TypedSayCommand, TypedClientCommand, CommandInfo
from commands import CommandReturn
from listeners import OnClientDisconnect
from colors import Color


_players_disable: Final[list[int]] = []


@OnClientDisconnect
def on_client_disconnect(index: int) -> None:
    global _players_disable

    try:
        _players_disable.remove(index)
    except ValueError:
        pass


@Event('player_spawn')
def on_player_spawn(event: GameEvent) -> None:
    global _players_disable

    player: Final[Player] = Player.from_userid(int(event['userid']))
    player_index: Final[int] = player.index

    player_block: Final[bool] = player_index not in _players_disable
    if player_block:
        player.color = Color(255, 255, 255, 200)
    else:
        player.color = Color(255, 255, 255, 255)

    player.set_noblock(player_block)


@TypedSayCommand('!noblock')
@TypedSayCommand('/noblock')
@TypedClientCommand('sm_noblock')
@TypedClientCommand('sp_noblock')
@TypedSayCommand('!block')
@TypedSayCommand('/block')
@TypedClientCommand('sm_block')
@TypedClientCommand('sp_block')
def on_no_block_cmd(info: CommandInfo) -> CommandReturn:
    global _players_disable

    player: Final[Player] = Player(info.index)
    player_index: Final[int] = player.index
    player_name: Final[str] = player.name

    player_block: Final[bool] = not player.get_noblock()
    if player_block:
        try:
            _players_disable.remove(player_index)
        except ValueError:
            pass
        player.color = Color(255, 255, 255, 200)
    else:
        _players_disable.append(player_index)
        player.color = Color(255, 255, 255, 255)

    player.set_noblock(player_block)
    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 has ' \
             + ('enabled' if player_block else 'disabled') \
             + ' \x05no block\x08!') \
        .send()

    return CommandReturn.BLOCK
