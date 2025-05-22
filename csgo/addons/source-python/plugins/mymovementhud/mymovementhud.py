from typing import Final, Any
from messages import SayText2, ShowMenu, HintText, TextMsg, HudMsg
from commands.typed import TypedSayCommand, TypedClientCommand, CommandInfo
from players.entity import Player
from menus import PagedMenu, PagedOption
from listeners import PlayerButtons, ButtonStatus, OnButtonStateChanged, get_button_combination_status
from colors import WHITE, GRAY, BLACK
from commands import CommandReturn


def load() -> None:
    SayText2('\x03>^< \x08| The \x09mymovementhud\x08 plugin is loaded!') \
        .send()


def unload() -> None:
    SayText2('\x03>^< \x08| The \x09mymovementhud\x08 plugin is unloaded!') \
        .send()


use_show_menu: bool = False
use_hint_text: bool = False
use_text_msg: bool = False
use_hud_msg: bool = False


def on_menu_select(m: PagedMenu, index: int, option: PagedOption) -> PagedMenu:
    global use_show_menu
    global use_hint_text
    global use_text_msg
    global use_hud_msg

    use_show_menu = True if option.value == 0 else False
    use_hint_text = True if option.value == 1 else False
    use_text_msg = True if option.value == 2 else False
    use_hud_msg = True if option.value == 3 else False

    return m


menu: Final[PagedMenu] = PagedMenu(
    title='Movement HUD',
    select_callback=on_menu_select
)

menu.append(PagedOption('Use `ShowMenu`', 0))
menu.append(PagedOption('Use `HintText`', 1))
menu.append(PagedOption('Use `TextMsg`', 2))
menu.append(PagedOption('Use `HudMsg`', 3))


is_jump_pressed: bool = False
is_duck_pressed: bool = False
is_forward_pressed: bool = False
is_back_pressed: bool = False
is_moveleft_pressed: bool = False
is_moveright_pressed: bool = False


@OnButtonStateChanged
def on_button_state_changed(player: Player, old_buttons: Any, new_buttons: Any) -> None:
    jump_status: ButtonStatus = get_button_combination_status(old_buttons, new_buttons, PlayerButtons.JUMP)
    duck_status: ButtonStatus = get_button_combination_status(old_buttons, new_buttons, PlayerButtons.DUCK)
    forward_status: ButtonStatus = get_button_combination_status(old_buttons, new_buttons, PlayerButtons.FORWARD)
    back_status: ButtonStatus = get_button_combination_status(old_buttons, new_buttons, PlayerButtons.BACK)
    moveleft_status: ButtonStatus = get_button_combination_status(old_buttons, new_buttons, PlayerButtons.MOVELEFT)
    moveright_status: ButtonStatus = get_button_combination_status(old_buttons, new_buttons, PlayerButtons.MOVERIGHT)

    global is_jump_pressed
    global is_duck_pressed
    global is_forward_pressed
    global is_back_pressed
    global is_moveleft_pressed
    global is_moveright_pressed

    if jump_status == ButtonStatus.PRESSED:
        is_jump_pressed = True
    elif jump_status == ButtonStatus.RELEASED:
        is_jump_pressed = False

    if duck_status == ButtonStatus.PRESSED:
        is_duck_pressed = True
    elif duck_status == ButtonStatus.RELEASED:
        is_duck_pressed = False

    if forward_status == ButtonStatus.PRESSED:
        is_forward_pressed = True
    elif forward_status == ButtonStatus.RELEASED:
        is_forward_pressed = False

    if back_status == ButtonStatus.PRESSED:
        is_back_pressed = True
    elif back_status == ButtonStatus.RELEASED:
        is_back_pressed = False

    if moveleft_status == ButtonStatus.PRESSED:
        is_moveleft_pressed = True
    elif moveleft_status == ButtonStatus.RELEASED:
        is_moveleft_pressed = False

    if moveright_status == ButtonStatus.PRESSED:
        is_moveright_pressed = True
    elif moveright_status == ButtonStatus.RELEASED:
        is_moveright_pressed = False

    jump_str: str = 'J' if is_jump_pressed else '-'
    duck_str: str = 'C' if is_duck_pressed else '-'
    forward_str: str = 'W' if is_forward_pressed else '-'
    back_str: str = 'S' if is_back_pressed else '-'
    moveleft_str: str = 'A' if is_moveleft_pressed else '-'
    moveright_str: str = 'D' if is_moveright_pressed else '-'

    menu_str: str = jump_str \
        + ' ' + forward_str \
        + ' ' + duck_str \
        + '\n' + moveleft_str \
        + ' ' + back_str \
        + ' ' + moveright_str

    global use_show_menu
    global use_hint_text
    global use_text_msg
    global use_hud_msg

    if use_show_menu:
        ShowMenu(menu_str) \
            .send(player.index)

    if use_hint_text:
        HintText(menu_str) \
            .send(player.index)

    if use_text_msg:
        TextMsg(menu_str) \
            .send(player.index)

    if use_hud_msg:
        HudMsg(menu_str, y=0.68, color1=WHITE) \
            .send(player.index)


@TypedSayCommand('!mhud')
@TypedSayCommand('/mhud')
@TypedClientCommand('sm_mhud')
@TypedClientCommand('sp_mhud')
def on_mhud_cmd(info: CommandInfo) -> CommandReturn:
    menu.send(info.index)

    return CommandReturn.BLOCK
