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

from events import Event, GameEvent
from messages import SayText2
from players.entity import Player


@Event('bomb_beginplant')
def on_bomb_begin_plant(event: GameEvent) -> None:
    player: Player = Player.from_userid(event['userid'])
    player_name: str = player.get_name()

    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 is started planting the bomb!') \
        .send()


@Event('bomb_abortplant')
def on_bomb_abort_plant(event: GameEvent) -> None:
    player: Player = Player.from_userid(event['userid'])
    player_name: str = player.get_name()

    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 is aborted planting the bomb!') \
        .send()
