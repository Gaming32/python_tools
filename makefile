##################################################################
# Compile cenviron.c into cenviron.dll--a shareable object file
# on Cygwin, which is loaded dynamically when first imported.
##################################################################

PYLIB = /usr/bin/python3.6
PYINC = /usr/local/include/python3.6

cenviron.dll: keyboard
	gcc keyboard.c -g -I$(PYINC) -shared  -L$(PYLIB) -lpython3.6 -o $@