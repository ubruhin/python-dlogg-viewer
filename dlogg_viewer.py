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
from dlogg_db import DLoggDbDownload
from pyqtgraph.Qt import QtGui
from dateutil import tz
import pyqtgraph as pg
import pandas as pd
import numpy as np
import datetime
import logging

log = logging.getLogger(__name__)


class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        pg.AxisItem.__init__(self, *args, **kwargs)
        self.setStyle(textFillLimits=[(0, 0.9)])

    def tickStrings(self, values, scale, spacing):
        return [pd.to_datetime(value, utc=True).tz_convert(tz.tzlocal())
                .strftime('%Y-%m-%d\n%H:%M:%S') for value in values]


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)

    with DLoggDbDownload(db_host, db_port, db_name, db_user, db_pw) as download:

        # fetch data from database
        end_utc = datetime.datetime.utcnow()
        start_utc = end_utc - datetime.timedelta(days=7)
        data = download.fetch_data_range(start_utc, end_utc)
        timestamps = [dt.astype(np.int64) for dt in data['inserted'].as_matrix()]

        # create window and legend
        app = QtGui.QApplication([])
        win = pg.GraphicsWindow(title="D-LOGG Data")
        win.resize(1280, 1024)
        legend = pg.LegendItem()

        # plot inputs
        plot_inputs = win.addPlot(row=0, col=0, axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        plot_inputs.setLabel('left', "Inputs")
        plot_inputs.showGrid(x=True, y=True, alpha=0.8)
        for i in range(0, 16):
            column = "input_{}".format(i + 1)
            name = u"I{}: {}".format(i + 1, input_names[i + 1])
            color = pg.intColor(i)
            curve = plot_inputs.plot(x=timestamps, y=data[column].as_matrix(), pen=color, name=name)
            legend.addItem(curve, name)

        # plot outputs
        plot_outputs = win.addPlot(row=1, col=0)
        plot_outputs.setLabel('left', "Outputs")
        plot_outputs.showGrid(x=True, y=True, alpha=0.8)
        plot_outputs.hideAxis('bottom')
        plot_outputs.setMaximumHeight(100)
        plot_outputs.setXLink(plot_inputs)
        for i in range(0, 13):
            column = "output_{}".format(i + 1)
            name = u"O{}: {}".format(i + 1, output_names[i + 1])
            color = pg.intColor(i)
            curve = plot_outputs.plot(x=timestamps, y=data[column].as_matrix(), pen=color, name=name)
            legend.addItem(curve, name)

        # plot pump speeds
        plot_pumps = win.addPlot(row=2, col=0)
        plot_pumps.setLabel('left', "Pump Speeds")
        plot_pumps.showGrid(x=True, y=True, alpha=0.8)
        plot_pumps.hideAxis('bottom')
        plot_pumps.setMaximumHeight(200)
        plot_pumps.setXLink(plot_inputs)
        for i in range(0, 4):
            column = "pump_speed_{}".format(i + 1)
            name = u"P{}: {}".format(i + 1, pump_names[i + 1])
            color = pg.intColor(i)
            curve = plot_pumps.plot(x=timestamps, y=data[column].as_matrix(), pen=color, name=name)
            legend.addItem(curve, name)

        # add legend
        legend_viewbox = win.addViewBox(rowspan=3)
        legend_viewbox.setMaximumWidth(220)
        legend.setParentItem(legend_viewbox)
        legend.anchor((0, 0), (0, 0))

        # show window
        QtGui.QApplication.instance().exec_()
