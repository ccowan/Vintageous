import unittest

from Vintageous.tests import set_text
from Vintageous.tests import add_sel
from Vintageous.tests import get_sel
from Vintageous.tests import first_sel
from Vintageous.tests import BufferTest

from Vintageous.vi.utils import modes


class Test_vi_big_s_InModeInternalNormal(BufferTest):
    def testDeletesWholeLine(self):
        set_text(self.view, ''.join(('foo bar\nfoo bar\nfoo bar\n',)))
        add_sel(self.view, self.R((1, 0), (1, 7)))

        self.view.run_command('_vi_big_s_action', {'mode': modes.INTERNAL_NORMAL})
        self.assertEqual(self.view.substr(self.R(0, self.view.size())), 'foo bar\n\nfoo bar\n')

    def testKeepsLeadingWhitespace(self):
        set_text(self.view, ''.join(('foo bar\n\t  foo bar\nfoo bar\n',)))
        add_sel(self.view, self.R((1, 0), (1, 10)))

        self.view.run_command('_vi_big_s_action', {'mode': modes.INTERNAL_NORMAL})
        self.assertEqual(self.view.substr(self.R(0, self.view.size())), 'foo bar\n\t  \nfoo bar\n')

    @unittest.skip("Implement")
    def testCanDeleteWithCount(self):
        self.assertTrue(False)
