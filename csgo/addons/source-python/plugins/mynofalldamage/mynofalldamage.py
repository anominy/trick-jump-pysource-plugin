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
from listeners import OnClientDisconnect


_players_enable: Final[list[int]] = []


@OnClientDisconnect
def on_client_disconnect(index: int) -> None:
    global _players_enable

    if index not in _players_enable:
        return

    _players_enable.remove(index)


@Event('player_falldamage')
def on_player_fall_damage(event: GameEvent) -> None:
    global _players_enable

    player: Final[Player] = Player.from_userid(int(event['userid']))
    player_index: Final[int] = player.index
    if player_index in _players_enable:
        return

    player_damage: Final[int] = int(event['damage'])
    player.health += player_damage


@TypedSayCommand('!falldamage')
@TypedSayCommand('/falldamage')
@TypedClientCommand('sm_falldamage')
@TypedClientCommand('sp_falldamage')
@TypedSayCommand('!fd')
@TypedSayCommand('/fd')
@TypedClientCommand('sm_fd')
@TypedClientCommand('sp_fd')
def on_fall_damage_cmd(info: CommandInfo) -> CommandReturn:
    global _players_enable

    player: Final[Player] = Player(info.index)
    player_index: Final[int] = player.index

    is_enabled: Final[bool] \
        = player_index in _players_enable
    if not is_enabled:
        _players_enable.remove(player_index)
    else:
        _players_enable.append(player_index)

    player_name: Final[str] = player.name
    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 is ' \
             + ('enabled' if is_enabled else 'disabled') \
             + ' \x05fall damage\x08!') \
         .send()

    return CommandReturn.BLOCK
