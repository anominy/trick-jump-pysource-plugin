@echo off

call :xcopy "%~dp0csgo" "%~dp0server\kty++trick\csgo"
exit /b 0

:xcopy
xcopy /k /r /e /i /s /c /h /f /o /x /y %*
exit /b
