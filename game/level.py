import pygame
from game.imports import import_csv_data, import_graphics
from game.settings import *
from game.tiles import Tile, GraphicTiles, Box, AnimatedTile


class Level:
    """
    Class for handling levels
    """
    def __init__(self, level_data, game_surface):
        """
        Initialize level setup
        Args:
            level_data: level data path we are importing from Tiled CSV file
            game_surface: screen the game is to be displayed on
        """
        # overall world setup
        self.display_surface = game_surface
        self.display_shift = 0

        # background setup
        background_data = import_csv_data(level_data['background'])
        self.background_sprites = self.create_tile_group(background_data, 'background')

        # terrain setup
        terrain_data = import_csv_data(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_data, 'terrain')

        # box setup
        box_data = import_csv_data(level_data['boxes'])
        self.box_sprites = self.create_tile_group(box_data, 'box')

        # fruits
        fruit_data = import_csv_data(level_data['fruits'])
        self.fruit_sprites = self.create_tile_group(fruit_data, 'fruits')

    def create_tile_group(self, layout, category):
        """
        create tile groups to display in world
        Args:
            layout: data imported from Tiles CSV file
            category: category of data to be imported
        Returns:
            sprite group that was created
        """
        sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != '-1':
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE

                    if category == 'background':
                        bg_tile_list = import_graphics('../graphics/backgrounds/backgrounds.png')
                        bg_surface = bg_tile_list[int(col)]
                        sprite = GraphicTiles(TILE_SIZE, x, y, bg_surface)

                    if category == 'terrain':
                        terrain_tile_list = import_graphics('../graphics/terrain/terrain.png')
                        terrain_surface = terrain_tile_list[int(col)]
                        sprite = GraphicTiles(TILE_SIZE, x, y, terrain_surface)

                    if category == 'box':
                        sprite = Box(TILE_SIZE, x, y)

                    if category == 'fruits':
                        sprite = AnimatedTile(TILE_SIZE, x, y, '../graphics/fruits/watermelon/Melon.png')

                    sprite_group.add(sprite)
        return sprite_group

    def run(self):
        """
        Run the level (display the sprites, make sure to put bottom layers first)
        """
        # background
        self.background_sprites.update(self.display_shift)
        self.background_sprites.draw(self.display_surface)
        # terrain
        self.terrain_sprites.update(self.display_shift)
        self.terrain_sprites.draw(self.display_surface)
        # boxes
        self.box_sprites.update(self.display_shift)
        self.box_sprites.draw(self.display_surface)
        # fruits
        self.fruit_sprites.update(self.display_shift)
        self.fruit_sprites.draw(self.display_surface)