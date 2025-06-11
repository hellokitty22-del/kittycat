import geo_features
from geo_features import Size, Location, Mountain, Lake, Crater
from robot import Robot

if __name__ == "__main__":

    # Load map and features
    size = Size()
    features = {}

    with open("geo_features.txt") as f:
        rows, cols = f.readline().split(",")
        size.height, size.width = int(rows), int(cols)

        for line in f:
            y, x, ftype, name, value = line.strip().split(",")
            loc = Location(int(y), int(x))
            value = int(value)
            if ftype == 'mountain':
                features[(loc.Y, loc.X)] = Mountain(loc, name, value)
            elif ftype == 'lake':
                features[(loc.Y, loc.X)] = Lake(loc, name, value)
            elif ftype == 'crater':
                features[(loc.Y, loc.X)] = Crater(loc, name, value)

    # Initialize robot
    robbie = Robot(size)

    while True:
        prompt = input("").strip()

        if prompt == 'quit':
            print("> goodbye")
            break

        elif prompt == 'show map':
            for i in range(size.height):
                row = ""
                for j in range(size.width):
                    f = features.get((i, j))
                    row += f.symbol() if f else '.'
                if i == 0:
                    print("> " + row)
                else:
                    print(row)
                

        elif prompt.startswith("info"):
            _, y, x = prompt.split()
            y, x = int(y), int(x)
            feature = features.get((y, x))
            print(feature if feature else "no information found")

        elif prompt.startswith("moveto"):
            _, y, x = prompt.split()
            y, x = int(y), int(x)
            robbie.move_to(Location(y, x))

        elif prompt == "explore":
            current_loc = (robbie.location.Y, robbie.location.X)
            feature = features.get(current_loc)
            if feature:
                robbie.explore(feature)
            else:
                print("> nothing to explore")

        elif prompt == "display journey":
            robbie.display_journey()

