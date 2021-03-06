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
from config import *
from window import DLoggViewerWindow
from dlogg_db import DLoggDbDownload
from pyqtgraph.Qt import QtGui
import datetime
import logging

log = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)

    with DLoggDbDownload(db_host, db_port, db_name, db_user, db_pw) as download:

        # fetch data from database
        end_utc = datetime.datetime.utcnow()
        start_utc = end_utc - datetime.timedelta(days=7)
        data = download.fetch_data_range(start_utc, end_utc)

        # show window
        app = QtGui.QApplication([])
        win = DLoggViewerWindow(data)
        win.show()
        QtGui.QApplication.instance().exec_()
