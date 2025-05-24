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
from events import Event, GameEvent
from players.entity import Player


_weapon_grenades: Final[tuple[str, ...]] = (
    'inferno',
    'hegrenade',
    # 'molotov',
    # 'decoy',
    # 'flashbang',
    # 'smokegrenade'
)


@Event('player_hurt')
def on_player_hurt(event: GameEvent) -> None:
    weapon_name: Final[str] = event['weapon']
    if weapon_name in _weapon_grenades:
        victim_user_id: Final[int] = int(event['userid'])
        victim_player: Final[Player] = Player.from_userid(victim_user_id)
        victim_player.health += int(event['dmg_health'])
