# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_oval, draw_rectangle, finish_drawing


def main():
    # Sizes in pixels
    scene_width = 800
    scene_height = 500
    cloud1_x0 = 85
    cloud1_y0 = 375
    cloud2_x0 = 140
    cloud2_y0 = 285

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas)
    draw_sun(canvas)
    draw_tree(canvas)
    draw_cloud(canvas, cloud1_x0, cloud1_y0, 1)
    draw_cloud(canvas, cloud2_x0, cloud2_y0, 1.6)

    # Call the finish_drawing function
    # in the draw2d.py library.

    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height, outline="", fill="lightSkyBlue1")


def draw_ground(canvas):
    x0 = -200
    y0 = 130
    x1 = 1000
    y1 = -300
    draw_oval(canvas, x0, y0, x1, y1, fill="springGreen3", outline="")


def draw_sun(canvas):
    x0 = 200
    y0 = 460
    x1 = 340
    y1 = 320
    draw_oval(canvas, x0, y0, x1, y1, fill="yellow1", outline="")


def draw_cloud(canvas, cloud_x0, cloud_y0, cloud_scale):
    top_left_x0 = cloud_x0
    top_left_y0 = cloud_y0
    top_left_x1 = top_left_x0 + 50 * cloud_scale
    top_left_y1 = top_left_y0 + 50 * cloud_scale
    draw_oval(canvas, top_left_x0, top_left_y0, top_left_x1,
              top_left_y1, fill="white", width=0, outline="")

    top_right_x0 = top_left_x0 + 35 * cloud_scale
    top_right_y0 = top_left_y0
    top_right_x1 = top_left_x1 + 35 * cloud_scale
    top_right_y1 = top_left_y1
    draw_oval(canvas, top_right_x0, top_right_y0, top_right_x1,
              top_right_y1, fill="white", width=0, outline="")

    bottom_left_x0 = top_left_x0 - 20 * cloud_scale
    bottom_left_y0 = top_left_y0 - 25 * cloud_scale
    bottom_left_x1 = top_left_x1 - 20 * cloud_scale
    bottom_left_y1 = top_left_y1 - 25 * cloud_scale
    draw_oval(canvas, bottom_left_x0, bottom_left_y0, bottom_left_x1,
              bottom_left_y1, fill="white", width=0, outline="")

    bottom_middle_x0 = bottom_left_x0 + 35 * cloud_scale
    bottom_middle_y0 = bottom_left_y0
    bottom_middle_x1 = bottom_left_x1 + 35 * cloud_scale
    bottom_middle_y1 = bottom_left_y1
    draw_oval(canvas, bottom_middle_x0, bottom_middle_y0, bottom_middle_x1,
              bottom_middle_y1, fill="white", width=0, outline="")

    bottom_right_x0 = bottom_left_x0 + 75 * cloud_scale
    bottom_right_y0 = bottom_left_y0
    bottom_right_x1 = bottom_left_x1 + 75 * cloud_scale
    bottom_Right_y1 = bottom_left_y1
    draw_oval(canvas, bottom_right_x0, bottom_right_y0, bottom_right_x1,
              bottom_Right_y1, fill="white", width=0, outline="")


def draw_tree_leaves(canvas, leaves_x0, leaves_y0, leaves_scale):
    top_left_x0 = leaves_x0 * leaves_scale
    top_left_y0 = leaves_y0 * leaves_scale
    top_left_x1 = top_left_x0 + 130 * leaves_scale
    top_left_y1 = top_left_y0 + 130 * leaves_scale
    draw_oval(canvas, top_left_x0, top_left_y0, top_left_x1,
              top_left_y1, fill="springGreen3", width=0, outline="")


def draw_tree_trunk(canvas, trunk_x0, trunk_y0):
    top_left_x0 = trunk_x0
    top_left_y0 = trunk_y0
    top_left_x1 = top_left_x0 + 40
    top_left_y1 = top_left_y0 - 160
    draw_rectangle(canvas, top_left_x0, top_left_y0, top_left_x1,
                   top_left_y1, fill="orange4", width=0, outline="")


def draw_tree_apple(canvas, apple_x0, apple_y0):
    top_left_x0 = apple_x0
    top_left_y0 = apple_y0
    top_left_x1 = top_left_x0 + 25
    top_left_y1 = top_left_y0 + 25
    draw_oval(canvas, top_left_x0, top_left_y0, top_left_x1,
              top_left_y1, fill="red2", width=0, outline="")


def draw_tree(canvas):
    leaves_x0 = 450
    leaves_y0 = 320
    trunk_x0 = 523
    trunk_y0 = 235
    apple_x0 = 510
    apple_y0 = 380
    draw_tree_leaves(canvas, leaves_x0, leaves_y0, 1)
    draw_tree_leaves(canvas, leaves_x0 - 10, leaves_y0 - 100, 1.2)
    draw_tree_leaves(canvas, leaves_x0 - 100, leaves_y0 - 140, 1.2)
    draw_tree_trunk(canvas, trunk_x0, trunk_y0)
    draw_tree_leaves(canvas, leaves_x0 + 70, leaves_y0 - 130, 1)
    draw_tree_apple(canvas, apple_x0, apple_y0)
    draw_tree_apple(canvas, apple_x0 + 80, apple_y0 - 80)
    draw_tree_apple(canvas, apple_x0 - 30, apple_y0 - 100)
    draw_tree_apple(canvas, apple_x0 - 80, apple_y0 - 320)


    # Call the main function so that
    # this program will start executing.
main()
