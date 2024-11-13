from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
ground = Entity(model="plane", collider="box", scale=64, texture="grass", texture_scale=(4, 4))

app.run()
