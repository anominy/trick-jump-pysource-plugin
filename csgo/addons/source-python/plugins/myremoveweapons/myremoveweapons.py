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
from commands.typed import TypedClientCommand, CommandInfo
from commands import CommandReturn
from players.entity import Player
from filters.entities import EntityIter
from filters.players import PlayerIter


def load() -> None:
    SayText2('\x03>^< \x08| The \x09myremoveweapons\x08 plugin is loaded!') \
        .send()


def unload() -> None:
    SayText2('\x03>^< \x08| The \x09myremoveweapons\x08 plugin is unloaded!') \
        .send()


@TypedClientCommand('drop')
def on_drop_cmd(info: CommandInfo) -> CommandReturn:
    player: Final[Player] = Player(info.index)
    player.get_active_weapon() \
        .remove()

    return CommandReturn.BLOCK


# def _remove_dropped_weapons() -> None:
#     weapon_indices: Final[list[int]] = []
#     for player in PlayerIter():
#         weapon_indices.extend(player.weapon_indexes())
#
#     for entity in EntityIter():
#         if entity.classname.startswith('weapon_'):
#             if entity.index in weapon_indices:
#                 continue
#
#             entity.remove()
