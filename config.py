#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# python-dlogg-viewer - Python script to visualize data from a D-LOGG device
# Copyright (C) 2017 U. Bruhin
# https://github.com/ubruhin/python-dlogg-viewer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

db_host = 'dlogg-db'
db_port = 3306
db_name = 'dlogg'
db_user = 'dlogg'
db_pw = 'dlogg'

input_names = {
    1: u"Kollektor",
    2: u"Puffer oben",
    3: u"Puffer unten",
    4: u"Warmwasser",
    5: u"Rücklauf Solar",
    6: u"Vorlauf Solar sekundär",
    7: u"Vorlauf Solar primär",
    8: u"Puffer oben (Anf. WP)",
    9: u"Puffer mitte (Anf. WP)",
    10: u"Rücklauf Wärmepumpe",
    11: u"-",
    12: u"Aussen",
    13: u"Vorlauf Heizkreis",
    14: u"Vorlauf Wärmepumpe",
    15: u"Raum",
    16: u"Volumenstrom Solar",
}

output_names = {
    1: u"Solarkreis sekundär",
    2: u"Ladepumpe Warmwasser",
    3: u"Ventil Topladung",
    4: u"Beladung oben (WP)",
    5: u"Wärmepumpe",
    6: u"Ladepumpe (WP)",
    7: u"Solarkreis primär",
    8: u"Heizkreismischer AUF",
    9: u"Heizkreismischer ZU",
    10: u"Heizkreispumpe",
    11: u"E-Heizung",
    12: u"Ausgang 12",
    13: u"Ausgang 13",
}

pump_names = {
    1: u"Pumpe 1",
    2: u"Pumpe 2",
    3: u"Pumpe 3",
    4: u"Pumpe 4",
}
