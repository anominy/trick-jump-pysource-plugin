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
    _remove_dropped_weapons()
    return CommandReturn.CONTINUE


def _remove_dropped_weapons() -> None:
    weapon_indices: Final[list[int]] = []
    for player in PlayerIter():
        for weapon in player.weapons():
            weapon_indices.append(weapon.index)

    for entity in EntityIter():
        if entity.classname.startswith('weapon_'):
            if entity.index in weapon_indices:
                continue

            entity.remove()
