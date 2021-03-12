class Point:
    x = 0
    y = 0

    def up(self, x):
        self.x += x

    def right(self, y):
        self.y += y

    def print(self):
        print(f'Y: {self.y} X: {self.x}')

    moves = {

    }


p = Point()
input_value = ''

while input_value != 'Treasure!':
    input_value = input('Enter direction & value\n')
    if input_value.split()[0] in ['North', 'South']:
        p.up(int(input_value.split()[1]))
    if input_value.split()[0] in ['East', 'West']:
        p.right(int(input_value.split()[1]))
p.print()
