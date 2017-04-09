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
from pyqtgraph.Qt import QtGui
from graph_widget import DLoggGraphWidget
import logging

log = logging.getLogger(__name__)


class DLoggViewerWindow(QtGui.QMainWindow):
    def __init__(self, data):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("D-LOGG Data")
        self.resize(1280, 1024)
        central_widget = QtGui.QWidget(self)
        self.setCentralWidget(central_widget)
        sidebar_layout = QtGui.QVBoxLayout()
        central_layout = QtGui.QHBoxLayout(central_widget)
        central_layout.setContentsMargins(3, 0, 0, 0)
        central_layout.addLayout(sidebar_layout)
        central_layout.addWidget(DLoggGraphWidget(data))

        check1 = QtGui.QCheckBox('hello')
        check1.stateChanged.connect(self.checkbox_checked_changed)
        sidebar_layout.addWidget(check1)

    def checkbox_checked_changed(self, state):
        print self.sender()
