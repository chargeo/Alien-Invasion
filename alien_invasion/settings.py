
class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialisze the game's static settings."""
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 5
		self.ship_limit = 3

		# Bullet settings
		self.bullet_width = 15
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 10

		# Alien settings
		self.fleet_drop_speed = 10

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# How quickly the alien poin values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

		# Scoring
		self.alien_points = 50


	def initialize_dynamic_settings(self):
		""" Initialize settings that change thoughout the game."""
		self.ship_speed = 5
		self.bullet_speed = 5
		self.alien_speed = 5

		# fleet direction of 1 erepresents right; -1 represents left.
		self.fleet_direction = 1

	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)


