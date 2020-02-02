import pygame
from pygame.mixer import Sound, Channel
from ..game.constants import *

class PygameSoundController:
	def __init__(self):
		pygame.mixer.init()

		self.movement_done = Sound("assets/sounds/robot-movement-F.ogg")
		self.movement_not_allowed = Sound("assets/sounds/robot-movement-C.ogg")
		self.kill_robot = Sound("assets/sounds/robot-movement-Ab.ogg")

		self.effect_channel = Channel(1)

	def play_sound_effect(self, sound):
		self.effect_channel.stop()
		self.effect_channel.play(sound)

	def trigger(self, event):
		if event == MOVEMENT_DONE:
			self.play_sound_effect(self.movement_done)

		if event == MOVEMENT_NOT_ALLOWED:
			self.play_sound_effect(self.movement_not_allowed)

		if event == KILL_ROBOT:
			self.play_sound_effect(self.kill_robot)

