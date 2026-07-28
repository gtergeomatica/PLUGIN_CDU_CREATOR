# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'assistenzagis@gter.it'
__date__ = '2019-07-18'
__copyright__ = 'Copyright 2019, Gter srl'

import unittest

from qgis.PyQt.QtGui import QDialogButtonBox, QDialog

from cdu_creator_dialog import CduCreatorDialog

from utilities import get_qgis_app
QGIS_APP = get_qgis_app()


class CduCreatorDialogTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        self.dialog = CduCreatorDialog(None)

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_dialog_ok(self):
        """Test we can click OK."""

        button = self.dialog.button_box.button(QDialogButtonBox.StandardButton.Ok)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.DialogCode.Accepted)

    def test_dialog_cancel(self):
        """Test we can click cancel."""
        button = self.dialog.button_box.button(QDialogButtonBox.StandardButton.Cancel)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.DialogCode.Rejected)

    def test_intcheckbox_exists_and_toggle(self):
        """The dialog should expose `IntcheckBox` and allow toggling."""
        # widget exists
        self.assertTrue(hasattr(self.dialog, 'IntcheckBox'))
        # default unchecked
        self.assertFalse(self.dialog.IntcheckBox.isChecked())
        # toggle
        self.dialog.IntcheckBox.setChecked(True)
        self.assertTrue(self.dialog.IntcheckBox.isChecked())

if __name__ == "__main__":
    suite = unittest.makeSuite(CduCreatorDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

