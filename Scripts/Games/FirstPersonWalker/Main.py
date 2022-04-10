from ursina.prefabs.first_person_controller import FirstPersonController
import ursina

app = ursina.Ursina()

ground = ursina.Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
player = FirstPersonController(z=-10, origin_y=-.5, speed=8)

app.run()