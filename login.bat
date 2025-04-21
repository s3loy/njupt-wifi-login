@echo off
:: 运行 curl 请求并输出结果
curl "https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%%2C0%%2C学号%%40运营商&user_password=你的密码"
echo.

:: 等待 3 秒
timeout /t 3 /nobreak >nul
exit
