from typing import Final
from messages import SayText2
from commands.typed import TypedSayCommand, TypedClientCommand, CommandInfo
from players.entity import Player
from commands import CommandReturn

import random


def load() -> None:
    SayText2('\x03>^< \x08| The \x09myroll\x08 plugin is loaded!') \
        .send()


def unload() -> None:
    SayText2('\x03>^< \x08| The \x09myroll\x08 plugin is unloaded!') \
        .send()


@TypedSayCommand('!roll')
@TypedSayCommand('/roll')
@TypedClientCommand('sm_roll')
@TypedClientCommand('sp_roll')
def on_roll_cmd(info: CommandInfo) -> CommandReturn:
    player: Final[Player] = Player(info.index)
    player_name: Final[str] = player.get_name()

    roll: Final[int] = random.randint(0, 100)
    SayText2('\x03>^< \x08| \x09' + player_name + '\x08 rolled \x05' + str(roll) + '\x08!') \
        .send()

    return CommandReturn.BLOCK
