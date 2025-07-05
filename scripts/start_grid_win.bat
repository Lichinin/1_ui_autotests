@echo off
setlocal enabledelayedexpansion

set SELENIUM_SERVER=./selenium-server
set HUB_PORT=4444
set NODE_COUNT=2
set HOST=127.0.0.1

echo Starting Hub on port %HUB_PORT%
start "Selenium Hub" java -jar "%SELENIUM_SERVER%" hub --port %HUB_PORT% --host %HOST%

timeout /t 5

for /L %%i in (1,1,%NODE_COUNT%) do (
    set /A PORT=5550 + %%i
    echo Starting Node %%i on port !PORT!
    start "Selenium Node %%i" java -jar "%SELENIUM_SERVER%" node --port !PORT! --hub http://%HOST%:%HUB_PORT% --host 192.168.56.1
)

echo.
echo Grid started: http://localhost:%HUB_PORT%/grid/console
endlocal