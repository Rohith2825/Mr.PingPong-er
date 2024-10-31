import unittest
import pygame
from  pingpongAI import Bar, Game  

class TestBar(unittest.TestCase):
    
    def setUp(self):
        # Setup for initializing a new bar and game instance for each test
        pygame.init()
        self.bar = Bar()
        self.game = Game()

    def test_bar_initialization(self):
        # Test initial position, score, and velocity values
        self.assertEqual(self.bar.length, 120)
        self.assertEqual(self.bar.height, 16)
        self.assertEqual(self.bar.score, 0)
        self.assertEqual(self.bar.fitness, 0)
        self.assertEqual(self.bar.bar_vel, 0)

    def test_bar_move_left(self):
        initial_x = self.bar.bar_x
        self.bar.moveLeft()
        self.assertLess(self.bar.bar_x, initial_x)

    def test_bar_move_right(self):
        initial_x = self.bar.bar_x
        self.bar.moveRight()
        self.assertGreater(self.bar.bar_x, initial_x)

    def test_ball_velocity_update(self):
        # Check if ball velocity updates correctly
        initial_x = self.bar.ball_center_x
        initial_y = self.bar.ball_center_y
        self.bar.updateVelocity()
        self.assertNotEqual(self.bar.ball_center_x, initial_x)
        self.assertNotEqual(self.bar.ball_center_y, initial_y)

    def test_collision_with_bar(self):
        # Simulate collision scenario and check if collision is detected
        self.bar.ball_center_y = Game.height - self.bar.height - self.bar.radius
        self.bar.ball_center_x = self.bar.bar_x + (self.bar.length // 2)
        self.assertTrue(self.bar.isColliding())

    def test_collision_with_walls(self):
        # Test collision with right wall
        self.bar.ball_center_x = Game.width
        self.assertTrue(self.bar.isCollidingSide())

        # Test collision with left wall
        self.bar.ball_center_x = 0
        self.assertTrue(self.bar.isCollidingSide())

    def test_predict_output(self):
        # Test the output of the predict method
        self.bar.ball_center_x = self.bar.center_x + 10  # Position ball in Quadrant I
        self.bar.ball_vel_x = 5
        self.bar.ball_vel_y = -5
        try:
            self.bar.predict()  # Run predict to check for any errors in decision making
        except Exception as e:
            self.fail(f"predict() raised an exception unexpectedly: {e}")

    def test_calculate_distance(self):
        # Test distance calculation between bar center and a specific point
        distance = self.bar.calculateDistance(self.bar.center_x, self.bar.center_y)
        self.assertEqual(distance, 0)
        # Test with a different point
        distance = self.bar.calculateDistance(self.bar.center_x + 10, self.bar.center_y)
        self.assertEqual(distance, 10)

class TestGame(unittest.TestCase):
    
    def setUp(self):
        pygame.init()
        self.game = Game()

    def test_initial_population(self):
        # Check if initial population of bars is created
        self.assertEqual(len(self.game.bars), Game.population)

    def test_generation_increment(self):
        # Simulate end of generation and check generation increment
        initial_gen = self.game.generation
        self.game.savedBars = self.game.bars.copy()  # Save all bars as "dead"
        self.game.bars = []
        self.game.gameLoop()
        self.assertGreater(self.game.generation, initial_gen)

    def test_highscore_tracking(self):
        # Check if highscore is recorded correctly
        self.game.highscore.append(50)
        self.game.highscore.append(100)
        self.assertEqual(max(self.game.highscore), 100)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
