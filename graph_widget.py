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

        # x-axis
        timestamps = [dt.astype(long) for dt in data['inserted'].as_matrix()]

        # inputs
        plot_inputs = self.addPlot(row=0, col=0, axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        plot_inputs.setLabel('left', "Inputs")
        plot_inputs.showGrid(x=True, y=True, alpha=0.8)
        for i in range(0, 16):
            column = "input_{}".format(i + 1)
            name = u"I{}: {}".format(i + 1, input_names[i + 1])
            color = pg.intColor(i)
            plot_inputs.plot(x=timestamps, y=data[column].as_matrix(), pen=color, name=name)

        # outputs
        plot_outputs = self.addPlot(row=1, col=0)
        plot_outputs.setLabel('left', "Outputs")
        plot_outputs.showGrid(x=True, y=True, alpha=0.8)
        plot_outputs.hideAxis('bottom')
        plot_outputs.setMaximumHeight(100)
        plot_outputs.setXLink(plot_inputs)
        for i in range(0, 13):
            column = "output_{}".format(i + 1)
            name = u"O{}: {}".format(i + 1, output_names[i + 1])
            color = pg.intColor(i)
            plot_outputs.plot(x=timestamps, y=data[column].as_matrix(), pen=color, name=name)

        # pump speeds
        plot_pumps = self.addPlot(row=2, col=0)
        plot_pumps.setLabel('left', "Pump Speeds")
        plot_pumps.showGrid(x=True, y=True, alpha=0.8)
        plot_pumps.hideAxis('bottom')
        plot_pumps.setMaximumHeight(200)
        plot_pumps.setXLink(plot_inputs)
        for i in range(0, 4):
            column = "pump_speed_{}".format(i + 1)
            name = u"P{}: {}".format(i + 1, pump_names[i + 1])
            color = pg.intColor(i)
            plot_pumps.plot(x=timestamps, y=data[column].as_matrix(), pen=color, name=name)
