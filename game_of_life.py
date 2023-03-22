"""
# TODO:
    1. add check of reccuring condition of the field
    2. add stop after p.1
"""

import time

class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.empty_f = []
        self.life_cells_start = []
        self.start_field = []

    def empty_field(self):
        for line in range(0, self.height):
            y = []
            for column in range(0, self.width):
                y.append('0')
            self.empty_f.append(y)
        return self.empty_f

    def start_fields(self, life_cells_start): # life_cells_start - [[row, cell],[row, cell]...]
        self.life_cells_start = life_cells_start
        start_field = self.empty_f
        for el in self.life_cells_start:
            start_field[el[0]][el[1]] = '1'
        return start_field

class Cell:
    def __init__(self, index_row, index_cell):
        self.coordinate_of_cell = []
        self.list_of_neighbors = []
        self.changeable = False
        self.index_row = index_row
        self.index_cell = index_cell
        self.value = ''
        self.count_of_live_neighbors = 0

    def coordinate(self):
        self.coordinate_of_cell.append(self.index_row)
        self.coordinate_of_cell.append(self.index_cell)
        return self.coordinate_of_cell

    def neighbors(self):
        c_left_cell = [self.coordinate_of_cell[0], self.coordinate_of_cell[1] - 1]
        self.list_of_neighbors.append(c_left_cell)
        c_right_cell = [self.coordinate_of_cell[0], self.coordinate_of_cell[1] + 1]
        self.list_of_neighbors.append(c_right_cell)

        u_left_cell = [self.coordinate_of_cell[0] - 1, self.coordinate_of_cell[1] - 1]
        self.list_of_neighbors.append(u_left_cell)
        u_cent_cell = [self.coordinate_of_cell[0] - 1, self.coordinate_of_cell[1]]
        self.list_of_neighbors.append(u_cent_cell)
        u_right_cell = [self.coordinate_of_cell[0] - 1, self.coordinate_of_cell[1] + 1]
        self.list_of_neighbors.append(u_right_cell)

        d_left_cell = [self.coordinate_of_cell[0] + 1, self.coordinate_of_cell[1] - 1]
        self.list_of_neighbors.append(d_left_cell)
        d_cent_cell = [self.coordinate_of_cell[0] + 1, self.coordinate_of_cell[1]]
        self.list_of_neighbors.append(d_cent_cell)
        d_right_cell = [self.coordinate_of_cell[0] + 1, self.coordinate_of_cell[1] + 1]
        self.list_of_neighbors.append(d_right_cell)

        i = 0
        for elements in self.list_of_neighbors:
            x = 0
            for el in elements:
                if el > 9:
                    self.list_of_neighbors[i][x] = 0
                if el < 0:
                    self.list_of_neighbors[i][x] = 9
                x += 1
            i += 1
        return self.list_of_neighbors

    def value_of_cell(self, field):
        self.value = field[self.coordinate_of_cell[0]][self.coordinate_of_cell[1]]
        return self.value

def work():
    field = Field(10, 10) # set start parameters of game field
    field.empty_field() # generate empty field
    game = field.start_fields([[3, 0], [3, 1], [2, 1], [1, 1], [2, 2]])
    while True:
        for el in game:
            print(el)

        index_row = 0
        list_of_change = []
        for row in game:
            index_cell = 0

            for cell in row:
                current_cell = Cell(index_row, index_cell)
                current_cell.coordinate()
                current_cell.neighbors()
                current_cell.value_of_cell(game)

                for neighbors in current_cell.list_of_neighbors:
                    neighbor = Cell(neighbors[0], neighbors[1])
                    neighbor.coordinate()
                    neighbor.value_of_cell(game)
                    if neighbor.value == '1':
                        current_cell.count_of_live_neighbors += 1

                if current_cell.value == '1':
                    if current_cell.count_of_live_neighbors != 3 and current_cell.count_of_live_neighbors != 2:
                        list_of_change.append(current_cell.coordinate_of_cell)

                if current_cell.value == '0':
                    if current_cell.count_of_live_neighbors == 3:
                        list_of_change.append(current_cell.coordinate_of_cell)
                index_cell += 1

            index_row += 1

        for change in list_of_change:
            value = game[change[0]][change[1]]
            if value == '1':
                game[change[0]][change[1]] = '0'
            else:
                game[change[0]][change[1]] = '1'
        print('__________________________________________')
        time.sleep(1)


if __name__ == '__main__':
    work()
