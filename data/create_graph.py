import json
import os
path_stations = r"subway_stations.json"
path_lines = r"subway_lines.json"
with open(path_stations, 'r',encoding="utf-8",errors="ignore") as file_stations:
    data_stations = json.load(file_stations)
with open(path_lines, 'r',encoding="utf-8",errors="ignore") as file_lines:
    data_lines = json.load(file_lines)
graph_in_use = {
    "graph":{
        "label":"Tehran Subway Network (in-use stations)",
        "type":"Transportation Network",
        "directed": False,
        "nodes":[x for x in data_stations if all(data_stations[x]["metadata"]["lines"][l]["state"]!="in use" for l in data_stations[x]["metadata"]["lines"])],
        "edges":[],
        "metadata":{"lines":{}}
    }
}
graph_all = {
    "graph":{
        "label":"Tehran Subway Network (all)",
        "type":"Transportation Network",
        "directed": False,
        "nodes":data_stations,
        "edges":[],
        "metadata":{"lines":{}}
    }
}
for line in data_lines:
    graph_all["graph"]["metadata"]["lines"][line] = data_lines[line]["metadata"]
    if data_lines[line]["metadata"]["state"] == "in use":
        graph_in_use["graph"]["metadata"]["lines"][line] = data_lines[line]["metadata"]
    else:
        continue

    for branch in data_lines[line]["branches"]:
        all_stations_list = data_lines[line]["branches"][branch]
        
        in_use_stations_list = [s for s in all_stations_list if data_stations[s]["metadata"]["lines"][line]["state"] == "in use"]

        for idx_station,station in enumerate(all_stations_list):
            if idx_station < len(all_stations_list)-1:
                next_station = all_stations_list[idx_station+1]
                new_edge = {
                    "source":station,
                    "target":next_station,
                    "metadata":{
                        "line":line,
                        "branch":branch
                    }                    
                }
                graph_all["graph"]["edges"].append(new_edge)
        for idx_station,station in enumerate(in_use_stations_list):
            if idx_station < len(in_use_stations_list)-1:
                next_station = in_use_stations_list[idx_station+1]
                new_edge = {
                    "source":station,
                    "target":next_station,
                    "metadata":{
                        "line":line,
                        "branch":branch
                    }                    
                }
                graph_in_use["graph"]["edges"].append(new_edge)
                

path_all = r"graph_all.json"
with open(path_all, 'w',encoding="utf-8",errors="ignore") as file_all:
    json.dump(graph_all,file_all,ensure_ascii=False,indent=4)

path_in_use = r"graph_in_use.json"
with open(path_in_use, 'w',encoding="utf-8",errors="ignore") as file_in_use:
    json.dump(graph_in_use,file_in_use,ensure_ascii=False,indent=4)

