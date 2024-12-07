import matplotlib.pyplot as plt
def create_polygon(points):
    points.sort()
    polygon = points + [points[0]]
    return polygon

def plot_polygon(polygon):
    x_coords, y_coords = zip(*polygon) #unpacks the polygon in x and y coordinates
    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, linestyle='-', color='b')
    plt.fill(x_coords, y_coords, 'b', alpha=0.3)
    plt.title("Polygon with the given points")
    plt.grid(True)
    plt.show()


points =[]
points.append((4,2))
points.append((7,-1))
points.append((3, -5))
points.append((-3,6))
points.append((-4,4))
points.append((-1,-1))
points.append((-2,-6))
polygon = create_polygon(points)
plot_polygon(polygon)