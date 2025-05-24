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

from typing import Final, Optional, Any
from events import Event, GameEvent
from messages import SayText2
from entities import CheckTransmitInfo
from entities.entity import Entity
from entities.helpers import index_from_edict
from entities.hooks import EntityCondition, EntityPreHook
from memory import make_object
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


@EntityPreHook(EntityCondition.is_player, 'set_transmit')
def on_pre_set_transmit(args: Any) -> Optional[bool]:
    global _players_enable

    entity: Final[Entity] = make_object(Entity, args[0])
    info: Final[CheckTransmitInfo] = make_object(CheckTransmitInfo, args[1])
    edict: Final[Any] = info.client
    player: Final[Player] = Player(index_from_edict(edict))

    if player.index == entity.index:
        return None

    if player.index in _players_enable:
        return False

    return None


@TypedSayCommand('!hide')
@TypedSayCommand('/hide')
@TypedClientCommand('sm_hide')
@TypedClientCommand('sp_hide')
def on_hide_cmd(info: CommandInfo) -> CommandReturn:
    global _players_enable

    player: Final[Player] = Player(info.index)
    player_index: Final[int] = player.index

    is_enable: Final[bool] \
        = player_index not in _players_enable
    if is_enable:
        _players_enable.append(player_index)
    else:
        _players_enable.remove(player_index)

    player_name: Final[str] = player.name
    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 is ' \
             + ('enabled' if is_enable else 'disabled') \
             + ' \x05hide\x08!') \
         .send()

    return CommandReturn.BLOCK
