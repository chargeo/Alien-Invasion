
class GameStats:
	""" Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statostics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an Inactive state.
		self.game_active = False

		# High Score should never be reset
		self.high_score = 0

	def reset_stats(self):
	    """Initialize statistics that can change durng the game."""
	    self.ships_left = self.settings.ship_limit
	    self.score = 0
	    self.level = 1