from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from reader import tup
class Voxel(Entity):
    def __init__(self, position=(0,0,0)):
        global array
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
            collider = 'cube',
        )
        array.append((self.position[0], self.position[1], self.position[2]))
    def input(self, key):
        global array,HoverMode
        if self.hovered:
            if HoverMode:
                hit_info = raycast(camera.world_position, camera.forward, distance=10)
                if hit_info.hit:
                    Voxel(position=hit_info.entity.position + hit_info.normal)
            if key == 'h':
                HoverMode = not HoverMode
            if key == 'left mouse down' and not HoverMode:
                Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                array = [el for el in array if el != self.position]
                destroy(self)

print("Loading world...")
array = tup(open('locations.txt', 'r'))
app = Ursina()
HoverMode = False
for i in range(len(array)):
    Voxel(position = array[i])
player = FirstPersonController()
WORLD = 20
def input(key):
    if key == 'u':
        fil = open('locations.txt', 'w')
        for el in array:
            fil.write(str(el) + "\n")

# def input(key):
#     if key == 'left mouse down':
#         hit_info = raycast(camera.world_position, camera.forward, distance=10)
#         if hit_info.hit:
#             Voxel(position=hit_info.entity.position + hit_info.normal)
Entity(model = 'sphere', color = color.azure, double_sided = True, scale = 150)
player = FirstPersonController()
app.run()