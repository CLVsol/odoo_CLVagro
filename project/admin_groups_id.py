#!/usr/bin/env python
# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from base import *

def Administrator_groups_id_clvagro():

    '''
    Reference: http://help.openerp.com/question/18704/hide-menu-for-existing-group/

    There are actually0-6 numbers for representing each job for a many2many/ one2many field

        (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
        (1, ID, { values }) -- update the linked record with id = ID (write values on it)
        (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the 
                   object completely, and the link to it as well)
        (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two 
                   objects but does not delete the target object itself)
        (4, ID) -- link to existing record with id = ID (adds a relationship)
        (5) -- unlink all (like using (3,ID) for all linked records)
        (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
    '''

    print 'Executing Administrator_groups_id_clvagro...'

    sock_common = xmlrpclib.ServerProxy(sock_common_url)
    uid = sock_common.login(dbname, admin_user, admin_user_pw)
    sock = xmlrpclib.ServerProxy(sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(dbname, uid, admin_user_pw, 'res.users', 'search', args)

    # clv_base
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Super User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Register Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Super Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_tag
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Tag User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Tag Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_annotation
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Annotation User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Annotation Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_document
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Document User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Document Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_pointing
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Pointing User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Pointing Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_place
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Place User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Place Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_frame
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Frame User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Frame Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_tray
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Tray User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Tray Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_batch
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Batch User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Batch Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    # clv_seedling
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Seedling User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Seedling Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'
