from main import Game, Graph, Ship, Position

game = Game()
game.update_map(load='3')

#game.print_map(waypoints=True)

#graph = Graph(game.map)
#game.update_map(load='3')
ship = game.my_ships[0]
#ship.planned_next_target = Position(5, 7, 0, 2)
game.graph.find_path(ship, Position(11,4), [Position(5,5)])
#graph.remove_node(11, 7)

#path = graph.find_path(Ship(1,13,7,4,1,100,graph), Position(12,7))

print()


