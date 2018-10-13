class AStarNode:

    def __init__(self, parent, layout,
                 empty_tile_index, name,
                 g_cost, h_cost):

        # Hash computed with all the tile values of the node.
        # Each node is unique.
        self.id = ''.join(chr(x + 97) for x in layout)

        self.parent = parent
        self.layout = layout
        self.empty_tile_index = empty_tile_index
        self.name = name

        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
