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

from typing import Any, Final
from events import Event, GameEvent
from messages import SayText2
from players.entity import Player
from entities.constants import DamageTypes
from cvars import cvar


def load() -> None:
    SayText2('\x03>^< \x08| The \x09myonehitkill\x08 plugin is loaded!') \
        .send()


def unload() -> None:
    SayText2('\x03>^< \x08| The \x09myonehitkill\x08 plugin is unloaded!') \
        .send()


@Event('player_hurt')
def on_player_hurt(event: GameEvent) -> None:
    victim_health: Final[int] = int(event['health'])
    if victim_health <= 0:
        return

    victim_user_id: Final[int] = int(event['userid'])
    attacker_user_id: Final[int] = int(event['attacker'])
    if not _is_valid_attack(victim_user_id, attacker_user_id):
        return

    victim_player: Final[Player] = Player.from_userid(victim_user_id)
    victim_player.health = 0


def _is_valid_attack(victim_user_id: int, attacker_user_id: int) -> bool:
    if victim_user_id == attacker_user_id:
        return False

    cvar_mp_teammates_are_enemies: Final[Any] = cvar.find_var('mp_teammates_are_enemies')
    mp_teammates_are_enemies: Final[int] = cvar_mp_teammates_are_enemies.get_int()

    victim_player: Final[Player] = Player.from_userid(victim_user_id)
    attacker_player: Final[Player] = Player.from_userid(attacker_user_id)

    victim_team: Final[int] = victim_player.get_team()
    attacker_team: Final[int] = attacker_player.get_team()

    return victim_team != attacker_team \
        or mp_teammates_are_enemies == 1
