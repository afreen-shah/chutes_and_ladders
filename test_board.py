import unittest
import board

class TestBoard(unittest.TestCase):
    """
    This class will test how we made the board
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
    """
    def test_chutes_dict(self): #passed
        """
        Testing board.make_chutes_and_ladders()
        this test sees if the chutes are all accurate to resembling a 'slide down'
        Since algorithm takes in the key and then moves the player to the value
        we will test to see that all keys are more than (therefore further up)
        than their associate value
        
        """
        result = board.make_chutes_and_ladders('chutes', board.red , 3)
        error_result = {key: value for key,value in result.items() if key < value} # this dictionary would consist of key value pairs that were incorrect (therefore any pairs wherekeys are less than (therefore further down) than their associate value)
        self.assertEqual(len(error_result), 0)

    def test_ladders_dict(self): #passed
        """
        Testing board.make_chutes_and_ladders()
        this test sees if the ladders are all accurate to resembling a 'climb up'
        Since algorithm takes in the key and then moves the player to the value
        we will test to see that all keys are less than (therefore further down)
        than their associate value
        """
        result = board.make_chutes_and_ladders('ladders', board.green , 3)
        error_result = {key: value for key,value in result.items() if key > value} # this dictionary would consist of key value pairs that were incorrect (therefore any pairs wherekeys are more than (therefore further up)than their associate value)
        self.assertEqual(len(error_result), 0 )


if __name__ == '__main__':
    unittest.main()