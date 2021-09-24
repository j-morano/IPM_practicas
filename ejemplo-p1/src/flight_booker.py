#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
import gettext
from pathlib import Path

from controller import Controller
from model import BookingData
from view import View

if __name__ == '__main__':

    # usamos el default locale en el resto de la ejecución
    # el default locale es el que tenga configurado la usuaria
    locale.setlocale(locale.LC_ALL, '')

    # Establecemos la BBDD de traducciones
    LOCALE_DIR = Path(__file__).parent / "locale"
    locale.bindtextdomain('FlightBooker', LOCALE_DIR)
    gettext.bindtextdomain('FlightBooker', LOCALE_DIR)
    gettext.textdomain('FlightBooker')

    controller = Controller()
    controller.set_model(BookingData())
    controller.set_view(View())
    controller.main()

