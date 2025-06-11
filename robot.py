import math
from geo_features import Location, Size, Mountain, Lake, Crater

class Robot:
    def __init__(self, map_size: Size):
        self.location = Location(0, 0)
        self.size = map_size
        self.day = 1
        self.logs = []
        # Initial exploration speeds
        self.exploration_speeds = {
            'mountain': 6,  # height units per day
            'lake': 8,      # depth units per day
            'crater': 10    # perimeter units per day
        }
    def move_to(self, dest: Location):
        if self.location == dest:
            print("> same location")
            return

        print(f"> move from ({self.location.Y},{self.location.X}) to ({dest.Y},{dest.X})")
        path = []
        curr = Location(self.location.Y, self.location.X)

        # Move in X first
        dx = (dest.X - curr.X) % self.size.width
        wrap_x = dx > self.size.width // 2
        if wrap_x:
            steps_x = (curr.X - dest.X) % self.size.width
            for _ in range(steps_x):
                curr.X = (curr.X - 1) % self.size.width
                path.append(Location(curr.Y, curr.X))
        else:
            for _ in range(dx):
                curr.X = (curr.X + 1) % self.size.width
                path.append(Location(curr.Y, curr.X))

        # Move in Y
        dy = (dest.Y - curr.Y) % self.size.height
        wrap_y = dy > self.size.height // 2
        if wrap_y:
            steps_y = (curr.Y - dest.Y) % self.size.height
            for _ in range(steps_y):
                curr.Y = (curr.Y - 1) % self.size.height
                path.append(Location(curr.Y, curr.X))
        else:
            for _ in range(dy):
                curr.Y = (curr.Y + 1) % self.size.height
                path.append(Location(curr.Y, curr.X))

        start_day = self.day
        for _ in path:
            self.day += 1
        end_day = self.day - 1

        path_str = f"move ({self.location.Y},{self.location.X})"
        for p in path:
            path_str += f" -> ({p.Y},{p.X})"

        self.logs.append((start_day, end_day, path_str))
        self.location = Location(dest.Y % self.size.height, dest.X % self.size.width)

    def display_journey(self):
        if not self.logs:
            return

        print(">", end=" ")
        for i, (start, end, desc) in enumerate(self.logs):
            if i == 0:
                # First line with '> ' prefix already printed
                if start == end:
                    print(f"Day {start}: {desc}")
                else:
                    print(f"Day {start}-{end}: {desc}")
            else:
                # Subsequent lines without prefix
                if start == end:
                    print(f"Day {start}: {desc}")
                else:
                    print(f"Day {start}-{end}: {desc}")

    def explore(self, feature):
        if not feature:
            print("> nothing to explore")
            return

        feature_type = type(feature).__name__.lower()
        name = getattr(feature, "name", "unknown")
        print(f"> explore {feature_type} {name}")

        # Calculate exploration time based on feature size and robot's speed
        feature_size = feature.get_size()
        speed = self.exploration_speeds[feature_type]
        
        # Calculate days needed (rounded up to nearest whole day)
        days_needed = math.ceil(feature_size / speed)

        start_day = self.day
        end_day = self.day + days_needed - 1
        self.day += days_needed

        # Log exploration
        path_str = f"explore {feature_type} {name}"
        self.logs.append((start_day, end_day, path_str))

        # Increase exploration speed by 20% for this feature type
        self.exploration_speeds[feature_type] *= 1.2
