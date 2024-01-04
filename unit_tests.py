import unittest
from run import calc_on_player_fitness, calc_on_player_random_perf, generate_top_5
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

class TestGenerateTop5(unittest.TestCase):
    def test_generate_top_5(self):
        team_list = [
            {'name': 'Player 1', 'pos': 'GK', 'perf': 80},
            {'name': 'Player 2', 'pos': 'DEF', 'perf': 85},
            {'name': 'Player 3', 'pos': 'MID', 'perf': 90},
            {'name': 'Player 4', 'pos': 'MID', 'perf': 95},
            {'name': 'Player 5', 'pos': 'ATT', 'perf': 85},
            {'name': 'Player 6', 'pos': 'ATT', 'perf': 90},
            {'name': 'Player 7', 'pos': 'DEF', 'perf': 80},
        ]
        mid_adj = 5
        att_adj = 10

        expected_output = [
            {'name': 'Player 4', 'pos': 'MID', 'perf': 95, 'top_5': 100},
            {'name': 'Player 6', 'pos': 'ATT', 'perf': 90, 'top_5': 100},
            {'name': 'Player 3', 'pos': 'MID', 'perf': 90, 'top_5': 95},
            {'name': 'Player 5', 'pos': 'ATT', 'perf': 85, 'top_5': 95},
            {'name': 'Player 2', 'pos': 'DEF', 'perf': 85, 'top_5': 85},
            {'name': 'Player 7', 'pos': 'DEF', 'perf': 80, 'top_5': 80},
                ]

        actual_output = generate_top_5(team_list, mid_adj, att_adj)

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
