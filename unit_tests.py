import unittest
from unittest.mock import MagicMock
from run import run_player_adj, calc_on_player_fitness, calc_on_player_random_perf

class TestCalcOnPlayerFitness(unittest.TestCase):
    def test_calc_on_player_fitness_gk(self):
        data = [
            {
                'pos': 'GK',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8
            }
        ]
        expected_data = [
            {
                'pos': 'GK',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8,
                'perf': 31
            }
        ]
        result = calc_on_player_fitness(data)
        self.assertEqual(result, expected_data)

    def test_calc_on_player_fitness_def(self):
        data = [
            {
                'pos': 'DEF',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8
            }
        ]
        expected_data = [
            {
                'pos': 'DEF',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8,
                'perf': 31
            }
        ]
        result = calc_on_player_fitness(data)
        self.assertEqual(result, expected_data)

    def test_calc_on_player_fitness_mid(self):
        data = [
            {
                'pos': 'MID',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8
            }
        ]
        expected_data = [
            {
                'pos': 'MID',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8,
                'perf': 31
            }
        ]
        result = calc_on_player_fitness(data)
        self.assertEqual(result, expected_data)

    def test_calc_on_player_fitness_other(self):
        data = [
            {
                'pos': 'ST',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8,
            }
        ]
        expected_data = [
            {
                'pos': 'ST',
                'fit': 90,
                'pa': 8,
                'co': 8,
                'sh': 9,
                'he': 7,
                'st': 8,
                'tk': 8,
                'ru': 7,
                'fl': 7,
                'cr': 8,
                'perf': 31
            }
        ]
        result = calc_on_player_fitness(data)
        self.assertEqual(result, expected_data)

class TestCalcOnPlayerRandomPerf(unittest.TestCase):
    def test_calc_on_player_random_perf(self):
        data = [
            {
                'perf': 80
            },
            {
                'perf': 90
            },
            {
                'perf': 70
            }
        ]
        result = calc_on_player_random_perf(data)
        for i in result:
            self.assertIn('adj_perf', i)
            self.assertGreaterEqual(i['adj_perf'], i['perf'] - 20)
            self.assertLessEqual(i['adj_perf'], i['perf'] + 20)

class TestRunPlayerAdj(unittest.TestCase):
    def test_run_player_adj(self):
        # Mock the calc_on_player_fitness and calc_on_player_random_perf functions
        calc_on_player_fitness_mock = MagicMock(return_value=[{'pos': 'GK', 'perf': 80}])
        calc_on_player_random_perf_mock = MagicMock(return_value=[{'pos': 'GK', 'adj_perf': 85}])
        
        # Replace the original functions with the mock functions
        original_calc_on_player_fitness = run.calc_on_player_fitness
        original_calc_on_player_random_perf = run.calc_on_player_random_perf
        run.calc_on_player_fitness = calc_on_player_fitness_mock
        run.calc_on_player_random_perf = calc_on_player_random_perf_mock
        
        # Define the input data
        hm = [{'pos': 'GK', 'fit': 90}]
        aw = [{'pos': 'GK', 'fit': 80}]
        
        # Define the expected output
        expected_hm_data_1 = [{'pos': 'GK', 'perf': 80}]
        expected_aw_data_1 = [{'pos': 'GK', 'adj_perf': 85}]
        
        # Call the function being tested
        result_hm_data_1, result_aw_data_1 = run_player_adj(hm, aw)
        
        # Assert that the mock functions were called with the correct arguments
        calc_on_player_fitness_mock.assert_called_once_with(hm)
        calc_on_player_random_perf_mock.assert_called_once_with(expected_hm_data_1)
        
        # Assert the output is as expected
        self.assertEqual(result_hm_data_1, expected_hm_data_1)
        self.assertEqual(result_aw_data_1, expected_aw_data_1)
        
        # Restore the original functions
        run.calc_on_player_fitness = original_calc_on_player_fitness
        run.calc_on_player_random_perf = original_calc_on_player_random_perf

if __name__ == '__main__':
    unittest.main()
