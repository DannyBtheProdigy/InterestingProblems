@echo off
setlocal EnableDelayedExpansion

echo %time%

set number=1
set sum=0

:natural_loop
	if %number% equ 1000 goto :end_problem
	set /a modulo_3="%number% %% 3"
	set /a modulo_5="%number% %% 5"
	set /a total_modulo="%modulo_3% * %modulo_5%"
	if %total_modulo% equ 0 (set /a sum="%sum% + %number%")
	set /a number="%number% + 1"	
	
	goto :natural_loop
	
	
:end_problem
	echo %time%

	echo %sum%
	pause