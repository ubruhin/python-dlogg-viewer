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

inputs = {
    1: (u"Kollektor", True),
    2: (u"Puffer oben", False),
    3: (u"Puffer unten", False),
    4: (u"Warmwasser", True),
    5: (u"Rücklauf Solar", False),
    6: (u"Vorlauf Solar sekundär", False),
    7: (u"Vorlauf Solar primär", False),
    8: (u"Puffer oben (Anf. WP)", False),
    9: (u"Puffer mitte (Anf. WP)", False),
    10: (u"Rücklauf Wärmepumpe", False),
    11: (u"-", False),
    12: (u"Aussen", True),
    13: (u"Vorlauf Heizkreis", False),
    14: (u"Vorlauf Wärmepumpe", False),
    15: (u"Raum", True),
    16: (u"Volumenstrom Solar", False),
}

outputs = {
    1: (u"Solarkreis sekundär", True),
    2: (u"Ladepumpe Warmwasser", True),
    3: (u"Ventil Topladung", True),
    4: (u"Beladung oben (WP)", False),
    5: (u"Wärmepumpe", False),
    6: (u"Ladepumpe (WP)", False),
    7: (u"Solarkreis primär", True),
    8: (u"Heizkreismischer AUF", True),
    9: (u"Heizkreismischer ZU", True),
    10: (u"Heizkreispumpe", True),
    11: (u"E-Heizung", False),
    12: (u"Ausgang 12", False),
    13: (u"Ausgang 13", False),
}

pumps = {
    1: (u"Pumpe 1", True),
    2: (u"Pumpe 2", True),
    3: (u"Pumpe 3", False),
    4: (u"Pumpe 4", True),
}
