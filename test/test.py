import unittest
from yambot.yam_bot import YamBot

# TODO: Should implement a bot with a test cog that launches commands that yambot can pick up
# TODO: Need a api key from discord, time to make another
class YamBotTestCase(unittest.TestCase):
    COMMAND_PREFIX = "."

    def setUp(self) -> None:
        # TODO: Launch yambot instance
        # TODO: Launch testbot instance
        test_yam = YamBot(self.COMMAND_PREFIX)
        test_yam.run("token")
    def test_my_test(self):
        self.assertEqual('foo'.upper(), 'FOO', "what the hell did you do?")
        self.assertTrue(True)


if __name__ == '__main__':
    test_classes = [YamBotTestCase]
    suites = []
    test_loader = unittest.TestLoader()

    for test_class in test_classes:
        suite = test_loader.loadTestsFromTestCase(test_class)
        suites.append(suite)

    master_suite = unittest.TestSuite(suites)
    unittest.TextTestRunner().run(master_suite)
