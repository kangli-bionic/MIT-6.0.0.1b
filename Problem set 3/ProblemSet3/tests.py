import unittest
from ps3b import *

class TestResitanceVirus(unittest.TestCase):
    def testWithDrugs(self):
        virus = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": False}, 0.0)
        child = virus.reproduce(0, ["drug2"])
        self.assertIsInstance(child, ResistantVirus, "Child is not a ResistantVirus")
        with self.assertRaises(NoChildException):
            child = virus.reproduce(0, ["drug1"])








