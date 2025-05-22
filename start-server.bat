@echo off

start "%~dp0start-server.bat" "%~dp0server\kty++trick\srcds.exe" ^
-console ^
-game csgo ^
-usercon ^
-nobreakpad ^
-insecure ^
-tickrate 64 ^
-maxplayers_override 4 ^
+hostname kty++trick ^
+sv_lan 1 ^
+map de_mirage
