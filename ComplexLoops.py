import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

arcade.open_window(400, 400, "Complex Loops - Box")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# Loop for each row
for row in range(10):
    # Loop for each column
    for column in range(10):
        # Calculate our location
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        # Draw the item
        if row % 2 == 0 and column % 2 == 0:
            arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, tilt_angle=45)
        elif row % 2 == 0 and column % 2 != 0:
            arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, tilt_angle=45)
        elif row % 2 != 0 and column % 2 == 0:
            arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, tilt_angle=45)
        elif row % 2 != 0 and column % 2 != 0:
            arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, tilt_angle=45)

arcade.finish_render()

arcade.run()
