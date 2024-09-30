#! /usr/bin/env python3

#inclusão de metadados
"""Hello Wordl Multi Language.

This program shows a message "Hello World", depends on the configuration 
of the enviroment LANG.

How to use:

Have the enviroment LANG configured (ex):
    export LANG=pt_BR

Execution
    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Renato Abreu"
__license__ = "Unlicense"

#importando módulo de sistema operacional
import os


# DECLARAÇÃO DE VARIAVEIS
current_language = os.getenv("LANG", "pt_BR")[:5]
msg = "Hello, World!"


if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "de_DE":
    msg = "Hallo Welt!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"


print(msg) 
