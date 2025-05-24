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
from paths import DATA_PATH
from players.entity import Player
from commands.typed import TypedSayCommand, TypedClientCommand, CommandInfo
from commands import CommandReturn
from geoip2.database import Reader as GeoIp2Reader
from geoip2.errors import AddressNotFoundError


@Event('player_spawn')
def on_player_spawn(event: GameEvent) -> None:
    player: Final[Player] = Player.from_userid(int(event['userid']))
    if player.is_fake_client() \
            or player.is_bot():
        return

    player_country: Final[str] = _get_player_country(player)
    player.clan_tag = '[' + player_country + ']'


@TypedSayCommand('!country')
@TypedSayCommand('/country')
@TypedClientCommand('sm_country')
@TypedClientCommand('sp_country')
def on_country_cmd(info: CommandInfo) -> CommandReturn:
    player: Final[Player] = Player(info.index)
    player_name: Final[str] = player.get_name()

    player_country: Final[str] = _get_player_country(player)
    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 is from \x05' + player_country + '\x08!') \
        .send()

    return CommandReturn.BLOCK


def _get_player_country(player: Player) -> str:
    return _get_country(player.address.split(':', 1)[0])


def _get_country(ip: str) -> str:
    result: str = 'N/A'
    if not ip:
        return result

    reader: Final[GeoIp2Reader] = GeoIp2Reader(DATA_PATH / 'custom/GeoLite2-City.mmdb')
    try:
        result = reader.city(ip).country
    except AddressNotFoundError:
        pass

    return result
