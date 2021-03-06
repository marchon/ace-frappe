# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals

import unittest, frappe
from frappe.utils import get_url

class TestAPI(unittest.TestCase):
	def test_insert_many(self):
		from frappe.frappeclient import FrappeClient

		frappe.db.sql('delete from `tabToDo` where description like "Test API%"')
		frappe.db.commit()

		host = get_url()

		if not host.startswith('http'):
			host = 'http://' + host

		if not host.endswith(':8000'):
			host = host + ':8000'

		server = FrappeClient(host, "Administrator", "admin", verify=False)

		server.insert_many([
			{"doctype": "ToDo", "description": "Test API 1"},
			{"doctype": "ToDo", "description": "Test API 2"},
			{"doctype": "ToDo", "description": "Test API 3"},
		])

		self.assertTrue(frappe.db.get_value('ToDo', {'description': 'Test API 1'}))
		self.assertTrue(frappe.db.get_value('ToDo', {'description': 'Test API 2'}))
		self.assertTrue(frappe.db.get_value('ToDo', {'description': 'Test API 3'}))
