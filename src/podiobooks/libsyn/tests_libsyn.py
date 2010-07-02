"""Automated Tests of the Podiobooks LibSyn Interface"""

# pylint: disable=C0103,C0111,R0904

from django.test import TestCase
from podiobooks.libsyn.libsyn_utils import get_show_info
import pprint

class LibsynTestCase(TestCase):
    # fixtures = []
    
    # def setUp(self):
    
    def testShowInfo(self):
        show_info = get_show_info('theflownsky')
        
        self.assertEquals('k-9b89823b4508200f', show_info['show_id'])
        
        # pretty print the result
        pprinter = pprint.PrettyPrinter(indent=4)
        pprinter.pprint(show_info)
        
        show_info = get_show_info('notesfromthevault')
        
        self.assertEquals('k-27813e6f24530266', show_info['show_id'])
        
        # pretty print the result
        pprinter = pprint.PrettyPrinter(indent=4)
        pprinter.pprint(show_info)