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

from typing import Final, Tuple
from types import MappingProxyType as MappingProxy
from messages import SayText2
from events import Event, GameEvent
from menus import PagedMenu, PagedOption
from commands.typed import TypedSayCommand, TypedClientCommand, CommandInfo
from players.entity import Player
from weapons.entity import Weapon
from commands import CommandReturn
from filters.entities import EntityIter
from listeners import OnClientDisconnect


def load() -> None:
    SayText2('\x03>^< \x08| The \x09myweapons\x08 plugin is loaded!') \
        .send()


def unload() -> None:
    SayText2('\x03>^< \x08| The \x09myweapons\x08 plugin is unloaded!') \
        .send()


_player_weapons: Final[dict[int, list[str]]] = {}


@OnClientDisconnect
def on_client_disconnect(index: int) -> None:
    global _player_weapons

    if index not in _player_weapons:
        return

    if index in _player_weapons:
        _player_weapons[index] \
            .clear()


@Event('player_death')
def on_player_death(event: GameEvent) -> None:
    for entity in EntityIter('weapon_c4'):
        entity.remove()


@Event('player_spawn')
def on_player_spawn(event: GameEvent) -> None:
    global _player_weapons

    player: Final[Player] = Player.from_userid(int(event['userid']))
    if player.is_fake_client() \
            or player.is_bot():
        return

    for weapon in player.weapons():
        weapon.remove()

    player_index: Final[int] = player.index
    if player_index not in _player_weapons:
        _player_weapons[player_index] = []

    for weapon_name in _player_weapons[player_index]:
        player.give_named_item(weapon_name)


# noinspection PyTypeChecker
_weapons: Final[dict[int, Tuple[str, str, int]]] = MappingProxy({
    0: ('weapon_ak47', 'AK-47', 1),
    1: ('weapon_m4a1', 'M4A4', 1),
    2: ('weapon_m4a1_silencer', 'M4A1-S', 1),
    3: ('weapon_famas', 'FAMAS', 1),
    4: ('weapon_galilar', 'Galil AR', 1),
    5: ('weapon_aug', 'AUG', 1),
    6: ('weapon_sg556', 'SG-553', 1),
    7: ('weapon_deagle', 'Desert Eagle', 2),
    8: ('weapon_revolver', 'R8 Revolver', 2),
    9: ('weapon_glock', 'Glock-18', 2),
    10: ('weapon_usp_silencer', 'USP-S', 2),
    11: ('weapon_cz75a', 'CZ75-Auto', 2),
    12: ('weapon_fiveseven', 'Five-SeveN', 2),
    13: ('weapon_p250', 'P250', 2),
    14: ('weapon_tec9', 'Tec-9', 2),
    15: ('weapon_elite', 'Dual Berettas', 2),
    16: ('weapon_hkp2000', 'P2000', 2),
    17: ('weapon_mp9', 'MP9', 1),
    18: ('weapon_mac10', 'MAC-10', 1),
    19: ('weapon_bizon', 'PP-Bizon', 1),
    20: ('weapon_mp7', 'MP7', 1),
    21: ('weapon_ump45', 'UMP-45', 1),
    22: ('weapon_p90', 'P90', 1),
    23: ('weapon_mp5sd', 'MP5-SD', 1),
    24: ('weapon_ssg08', 'SSG-80', 1),
    25: ('weapon_awp', 'AWP', 1),
    26: ('weapon_scar20', 'SCAR-20', 1),
    27: ('weapon_g3sg1', 'G3SG1', 1),
    28: ('weapon_nova', 'Nova', 1),
    29: ('weapon_xm1014', 'XM1014', 1),
    30: ('weapon_mag7', 'MAG-7', 1),
    31: ('weapon_sawedoff', 'Sawed-Off', 1),
    32: ('weapon_m249', 'M249', 1),
    33: ('weapon_negev', 'Negev', 1),
    34: ('weapon_decoy', 'Decoy', 3),
    35: ('weapon_flashbang', 'Flashbang Grenade', 3),
    36: ('weapon_smokegrenade', 'Smoke Grenade', 3),
    37: ('weapon_hegrenade', 'HE Grenade', 3),
    38: ('weapon_molotov', 'Molotov', 3),
    39: ('weapon_incgrenade', 'Incgrenade', 3),
    40: ('weapon_c4', 'C4 bomb', 5),
    41: ('weapon_taser', 'Zeus', 4),
    42: ('weapon_knife', 'Knife', 4)
})

_menu_options: Final[list[PagedOption]] \
    = [PagedOption(v[1], k) for k, v in _weapons.items()]

_menu: Final[PagedMenu] = PagedMenu(
    _menu_options,
    title='Weapons'
)


@_menu.register_select_callback
def menu_select_callback(menu: PagedMenu, index: int, option: PagedOption) -> PagedMenu:
    global _player_weapons

    selected_weapon: Final[str] = _weapons[option.value][0]
    selected_weapon_type: Final[int] = _weapons[option.value][2]

    player: Final[Player] = Player(index)
    if index not in _player_weapons:
        _player_weapons[index] = []

    for weapon in player.weapons():
        weapon_type: int = _get_weapon_type(weapon.classname)
        if weapon_type == selected_weapon_type:
            try:
                _player_weapons[index] \
                        .remove(weapon.weapon_name)
            except ValueError:
                pass
            weapon.remove()

    player.give_named_item(selected_weapon)
    _player_weapons[index] \
        .append(selected_weapon)

    return menu


@TypedClientCommand('drop')
def on_drop_cmd(info: CommandInfo) -> CommandReturn:
    global _player_weapons

    player: Final[Player] = Player(info.index)
    player_index: Final[int] = player.index
    player_weapon: Final[Weapon] = player.get_active_weapon()

    if player_weapon is None:
        return CommandReturn.BLOCK

    if player_index not in _player_weapons:
        _player_weapons[player_index] = []

    try:
        _player_weapons[player_index] \
            .remove(player_weapon.weapon_name)
    except ValueError:
        pass
    player_weapon.remove()

    return CommandReturn.BLOCK


def _get_weapon_type(weapon_class: str) -> int:
    for _, v in _weapons.items():
        if weapon_class == v[0]:
            return v[2]

    return 0


@TypedSayCommand('!weapons')
@TypedSayCommand('/weapons')
@TypedClientCommand('sm_weapons')
@TypedClientCommand('sp_weapons')
@TypedSayCommand('!weapon')
@TypedSayCommand('/weapon')
@TypedClientCommand('sm_weapon')
@TypedClientCommand('sp_weapon')
@TypedSayCommand('!guns')
@TypedSayCommand('/guns')
@TypedClientCommand('sm_guns')
@TypedClientCommand('sp_guns')
@TypedSayCommand('!gun')
@TypedSayCommand('/gun')
@TypedClientCommand('sm_gun')
@TypedClientCommand('sp_gun')
def on_weapons_cmd(info: CommandInfo) -> CommandReturn:
    global _menu
    _menu.send(info.index)

    return CommandReturn.BLOCK
