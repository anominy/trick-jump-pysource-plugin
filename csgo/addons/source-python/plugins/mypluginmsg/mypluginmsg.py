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

from messages import SayText2
from listeners import OnPluginLoaded, OnPluginUnloaded
from plugins.instance import Plugin


@OnPluginLoaded
def on_plugin_loaded(plugin: Plugin) -> None:
    SayText2('\x03>^< \x08| The \x09' + plugin.name + '\x08 plugin is loaded!') \
        .send()


@OnPluginUnloaded
def on_plugin_unloaded(plugin: Plugin) -> None:
    SayText2('\x03>^< \x08| The \x09' + plugin.name + '\x08 plugin is unloaded!') \
        .send()
