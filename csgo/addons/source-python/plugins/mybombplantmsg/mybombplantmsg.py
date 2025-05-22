from events import Event, GameEvent
from messages import SayText2
from players.entity import Player


def load() -> None:
    SayText2('\x03>^< \x08| The \x09mybombplantmsg\x08 plugin is loaded!') \
        .send()


def unload() -> None:
    SayText2('\x03>^< \x08| The \x09mybombplantmsg\x08 plugin is unloaded!') \
        .send()


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
