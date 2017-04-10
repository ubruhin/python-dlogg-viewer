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
from dateutil import tz
import pyqtgraph as pg
import pandas as pd
import logging

log = logging.getLogger(__name__)


class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        pg.AxisItem.__init__(self, *args, **kwargs)
        self.setStyle(textFillLimits=[(0, 0.9)])

    def tickStrings(self, values, scale, spacing):
        return [pd.to_datetime(value, utc=True).tz_convert(tz.tzlocal())
                .strftime('%Y-%m-%d\n%H:%M:%S') for value in values]


class DLoggGraphWidget(pg.GraphicsLayoutWidget):
    def __init__(self, data):
        pg.GraphicsLayoutWidget.__init__(self)
        self._data = data

        # x-axis
        self._timestamps = [dt.astype(long) for dt in self._data['inserted'].as_matrix()]

        # inputs
        self._plot_inputs = self.addPlot(row=0, col=0, axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        self._plot_inputs.setLabel('left', "Inputs")
        self._plot_inputs.showGrid(x=True, y=True, alpha=0.8)

        # outputs
        self._plot_outputs = self.addPlot(row=1, col=0)
        self._plot_outputs.setLabel('left', "Outputs")
        self._plot_outputs.showGrid(x=True, y=True, alpha=0.8)
        self._plot_outputs.hideAxis('bottom')
        self._plot_outputs.setMaximumHeight(100)
        self._plot_outputs.setXLink(self._plot_inputs)

        # pump speeds
        self._plot_pumps = self.addPlot(row=2, col=0)
        self._plot_pumps.setLabel('left', "Pump Speeds")
        self._plot_pumps.showGrid(x=True, y=True, alpha=0.8)
        self._plot_pumps.hideAxis('bottom')
        self._plot_pumps.setMaximumHeight(200)
        self._plot_pumps.setXLink(self._plot_inputs)

    def add_input(self, index, name, color):
        column = "input_{}".format(index + 1)
        return self._plot_inputs.plot(x=self._timestamps, y=self._data[column].as_matrix(), pen=color, name=name)

    def add_output(self, index, name, color):
        column = "output_{}".format(index + 1)
        return self._plot_outputs.plot(x=self._timestamps, y=self._data[column].as_matrix(), pen=color, name=name)

    def add_pump_speed(self, index, name, color):
        column = "pump_speed_{}".format(index + 1)
        return self._plot_pumps.plot(x=self._timestamps, y=self._data[column].as_matrix(), pen=color, name=name)
