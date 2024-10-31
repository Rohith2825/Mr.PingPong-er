import unittest
import pygame
from pingpongAI import Bar, Game, GA  # Replace `your_module_name` with the actual module name

class IntegrationTestGame(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.game = Game()
        self.ga = GA(self.game)

    def test_game_initialization(self):
        # Check if the game initializes correctly with the right settings
        self.assertEqual(self.game.width, 900)
        self.assertEqual(self.game.height, 600)
        self.assertEqual(len(self.game.bars), self.game.population)
        self.assertEqual(self.game.generation, 1)

    def test_bar_and_game_interaction(self):
        # Check if bars interact with the game environment as expected
        for bar in self.game.bars:
            bar.predict()
            bar.updateVelocity()
            bar.showBar(bar.bar_x, bar.bar_y)
            bar.showBall(bar.ball_center_x, bar.ball_center_y)
            # Ensure the bar stays within the game width boundaries
            self.assertTrue(0 <= bar.bar_x <= Game.width - bar.length)

    def test_collision_detection_integration(self):
        # Check if collision detection works for bar-ball interaction and ball-wall interaction
        for bar in self.game.bars:
            # Simulate ball hitting the bar
            bar.ball_center_y = Game.height - bar.height - bar.radius
            bar.ball_center_x = bar.bar_x + (bar.length // 2)
            self.assertTrue(bar.isColliding())

            # Simulate ball hitting the walls
            bar.ball_center_x = Game.width
            self.assertTrue(bar.isCollidingSide())
            bar.ball_center_x = 0
            self.assertTrue(bar.isCollidingSide())

            # Simulate ball hitting the top boundary
            bar.ball_center_y = 0
            self.assertTrue(bar.isCollidingAbove())

    def test_predict_and_move_integration(self):
        # Test if AI predictions lead to expected movement outcomes
        for bar in self.game.bars:
            initial_position = bar.bar_x
            bar.predict()
            # Check if the prediction moved the bar left or right
            self.assertNotEqual(bar.bar_x, initial_position)

    def test_ga_generation_evolution(self):
        # Check if GA properly evolves generations and updates the game state
        # Simulate the end of a generation
        initial_generation = self.game.generation
        self.game.savedBars = self.game.bars.copy()  # Mark all bars as "dead"
        self.game.bars = []
        
        self.ga.nextGen()
        
        # Check if the generation count increments
        self.assertEqual(self.game.generation, initial_generation + 1)
        # Ensure the population of bars is replenished
        self.assertEqual(len(self.game.bars), self.game.population)

    def test_highscore_tracking_integration(self):
        # Ensure high scores are tracked and saved across generations
        self.game.highscore.append(10)
        self.game.highscore.append(50)
        self.game.highscore.append(100)
        
        # Simulate a high score being achieved in a generation
        self.game.savedBars = [Bar() for _ in range(self.game.population)]
        for bar in self.game.savedBars:
            bar.score = 200  # Simulate a high score for all bars
        self.ga.calculateFitness()  # This should update fitness values based on score

        # Ensure the high score is updated
        self.assertEqual(max(self.game.highscore), 200)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
