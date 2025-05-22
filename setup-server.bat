@echo off

:: The `+force_install_dir "<dpath>"` must be
::  executed before the `+login <mparam>` command
:: ----------------------------------------------
:: Otherwise `steamcmd.exe` will display a warning

start "%~dp0setup-server.bat" cmd /c steamcmd.exe ^
+@ShutdownOnFailedCommand 1 ^
+@NoPromptForPassword 1 ^
+force_install_dir "%~dp0server\kty++trick" ^
+login anonymous ^
+app_update 740 ^
+quit  ^& echo; ^& pause
