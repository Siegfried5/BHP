# Volatility
# Copyright (C) 2007-2013 Volatility Foundation
#
# This file is part of Volatility.
#
# Volatility is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License Version 2 as
# published by the Free Software Foundation.  You may not use, modify or
# distribute this program under any other version of the GNU General
# Public License.
#
# Volatility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Volatility.  If not, see <http://www.gnu.org/licenses/>.
#

"""
@author:       Andrew Case
@license:      GNU General Public License 2.0
@contact:      atcuno@gmail.com
@organization: 
"""

import volatility.obj as obj
import volatility.plugins.mac.common as common

class mac_lsmod(common.AbstractMacCommand):
    """ Lists loaded kernel modules """

    def calculate(self):
        common.set_plugin_members(self)

        p = self.addr_space.profile.get_symbol("_kmod")
        kmodaddr = obj.Object("Pointer", offset = p, vm = self.addr_space)
        kmod = kmodaddr.dereference_as("kmod_info") 

        while kmod.is_valid():
            yield kmod
            kmod = kmod.next

    def render_text(self, outfd, data):
        self.table_header(outfd, [("Address", "[addrpad]"), 
                                  ("Size", "[addr]"), 
                                  ("Refs", "^8"),
                                  ("Version", "12"),  
                                  ("Name", "")])
        for kmod in data:
            self.table_row(outfd, 
                           kmod.address, 
                           kmod.m('size'), 
                           kmod.reference_count, 
                           kmod.version, 
                           kmod.name)
