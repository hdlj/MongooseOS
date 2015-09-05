#=============================================================================
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>'''
#
#    Date: 2015
#
#===============================================================================




#
# MOSInterfaceC . py
# Declare here global variables and functions which need to be
# accessible by Python applications
# MOSInterfaceFDD maps function names to their return type
# MOSInterfaceGVD maps global variable to their return type
# Only float , uint8 t , uint16 t , string and CList can be used 
#



MOSInterfaceFDD = {}

MOSInterfaceFDD["sin"] = "float"
MOSInterfaceFDD["cos"] = "float"

# C/C++ functions ’ declaration
#...

MOSInterfaceGVD = {}
MOSInterfaceGVD["M_PI"] = "float"
# C/C++ global variables
#...
