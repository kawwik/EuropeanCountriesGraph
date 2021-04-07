from igraph import *

graph = Graph(47)  # Создаём граф на 47 вершин
graph.vs["name"] = [
    "Albania",
    "Andorra",
    "Austria",
    "Belarus",
    "Belgium",
    "BaH",
    "Bulgaria",
    "Croatia",
    "Cypruse",
    "Czech",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Kosovo",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Malta",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Russia",
    "San_Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "Turkey",
    "Ukraine",
    "UK",
    "Vatican"]  # Именуем все вершины в алфавитном порядке

CMap = {
    "Albania": 0,
    "Andorra": 1,
    "Austria": 2,
    "Belarus": 3,
    "Belgium": 4,
    "BaH": 5,
    "Bulgaria": 6,
    "Croatia": 7,
    "Cypruse": 8,
    "Czech": 9,
    "Denmark": 10,
    "Estonia": 11,
    "Finland": 12,
    "France": 13,
    "Germany": 14,
    "Greece": 15,
    "Hungary": 16,
    "Iceland": 17,
    "Ireland": 18,
    "Italy": 19,
    "Kosovo": 20,
    "Latvia": 21,
    "Liechtenstein": 22,
    "Lithuania": 23,
    "Luxembourg": 24,
    "Macedonia": 25,
    "Malta": 26,
    "Moldova": 27,
    "Monaco": 28,
    "Montenegro": 29,
    "Netherlands": 30,
    "Norway": 31,
    "Poland": 32,
    "Portugal": 33,
    "Romania": 34,
    "Russia": 35,
    "San_Marino": 36,
    "Serbia": 37,
    "Slovakia": 38,
    "Slovenia": 39,
    "Spain": 40,
    "Sweden": 41,
    "Switzerland": 42,
    "Turkey": 43,
    "Ukraine": 44,
    "UK": 45,
    "Vatican": 46
} #Словарь {название страны : номер вершины}

# Загружаем граф с помощью списка смежности из файла
edges = open("Edges.txt", 'r')
for line in edges:
    splitLine = line.split()
    country = CMap[splitLine[0]]
    for neighbour in splitLine[2::]:
        graph.add_edge(country, CMap[neighbour])
edges.close()
graph.simplify() # Удаляем кратные рёбра

# Удаляем вершины, не входящие в наибольшую компоненту:
verticesToDel = [v for v in range(47) if v not in min(graph.components())]
graph.delete_vertices(verticesToDel)

# Изменяем словарь вершин в соответствии с удалёнными вершинами
CMap.clear()
for i in range(graph.vcount()):
    CMap[graph.vs[i]['name']] = i

# (b)
vPower = graph.vcount()
ePower = graph.ecount()
minDeg = min(graph.degree())
maxDeg = max(graph.degree())
radius = graph.radius()
diameter = graph.diameter()
girth = graph.girth()
center = [graph.vs['name'][v] for v in range(vPower) if graph.eccentricity(v) == radius]
vertexConnectivity = graph.vertex_connectivity()
edgesConnectivity = graph.edge_connectivity()

# (e)
maximumCliques = graph.largest_cliques()

# (f)
maximumStableSets = graph.largest_independent_vertex_sets()

# (l)
components = graph.biconnected_components()

# (o)
# Добавляем рёбрам веса
weights = open("Distances.txt", 'r')
for line in weights:
    vertex1, vertex2 = line.split()[:2]
    weight = line.split()[2]
    graph.es.find(_from=vertex1, _to=vertex2)['weight'] = weight
