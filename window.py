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
from graph_widget import DLoggGraphWidget
from pyqtgraph.Qt import QtGui
import pyqtgraph as pg
import logging

log = logging.getLogger(__name__)


class ColoredCheckbox(QtGui.QWidget):
    def __init__(self, name, color, checked, slot):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self._cbx = QtGui.QCheckBox(self)
        self._cbx.setChecked(checked)
        self._cbx.setFixedWidth(50)
        self._cbx.setStyleSheet("background-color: {};".format(color.name()))
        self._cbx.stateChanged.connect(slot)
        layout.addWidget(self._cbx)
        layout.addWidget(QtGui.QLabel(name, self))

    def isChecked(self):
        return self._cbx.isChecked()


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
        graph = DLoggGraphWidget(data)
        central_layout.addWidget(graph)
        self._curve_checkboxes = list()

        for i in range(0, 16):
            name = u"I{}: {}".format(i + 1, inputs[i + 1][0])
            color = self._color_by_index(i)
            cbx = ColoredCheckbox(name, color, inputs[i + 1][1], self._checked_changed)
            self._curve_checkboxes.append((graph.add_input(i, name, color), cbx))
            sidebar_layout.addWidget(cbx)
        sidebar_layout.addWidget(self._create_horizontal_line())

        for i in range(0, 13):
            name = u"O{}: {}".format(i + 1, outputs[i + 1][0])
            color = self._color_by_index(i)
            cbx = ColoredCheckbox(name, color, outputs[i + 1][1], self._checked_changed)
            sidebar_layout.addWidget(cbx)
            self._curve_checkboxes.append((graph.add_output(i, name, color), cbx))
        sidebar_layout.addWidget(self._create_horizontal_line())

        for i in range(0, 4):
            name = u"P{}: {}".format(i + 1, pumps[i + 1][0])
            color = self._color_by_index(i)
            cbx = ColoredCheckbox(name, color, pumps[i + 1][1], self._checked_changed)
            sidebar_layout.addWidget(cbx)
            self._curve_checkboxes.append((graph.add_pump_speed(i, name, color), cbx))

        self._checked_changed()

    def _color_by_index(self, index):
        return pg.intColor(index)

    def _create_horizontal_line(self):
        frame = QtGui.QFrame(self)
        frame.setFrameShape(QtGui.QFrame.HLine)
        return frame

    def _checked_changed(self):
        for curve, checkbox in self._curve_checkboxes:
            curve.setVisible(checkbox.isChecked())
