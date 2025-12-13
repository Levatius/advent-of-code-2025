from collections import defaultdict

import networkx as nx


def parse(lines: list[str]) -> nx.DiGraph:
    devices = nx.DiGraph()
    for line in lines:
        device, other_devices_str = line.split(": ")
        for other_device in other_devices_str.split():
            devices.add_edge(device, other_device)
    return devices


def count_paths_in_dag(devices: nx.DiGraph, source: str, target: str) -> int:
    paths = defaultdict(int)
    paths[source] = 1
    for node in nx.topological_sort(devices):
        for successor in devices.successors(node):
            paths[successor] += paths[node]
    return paths[target]


def part_1(devices: nx.DiGraph) -> int:
    # Devices must be a DAG to work
    assert nx.is_directed_acyclic_graph(devices)

    return count_paths_in_dag(devices, "you", "out")


def part_2(devices: nx.DiGraph) -> int:
    # Devices must be a DAG to work
    assert nx.is_directed_acyclic_graph(devices)

    # Paths where fft is visited before dac
    svr_fft = count_paths_in_dag(devices, "svr", "fft")
    fft_dac = count_paths_in_dag(devices, "fft", "dac")
    dac_out = count_paths_in_dag(devices, "dac", "out")

    # Paths where dac is visited before fft
    svr_dac = count_paths_in_dag(devices, "svr", "dac")
    dac_fft = count_paths_in_dag(devices, "dac", "fft")
    fft_out = count_paths_in_dag(devices, "fft", "out")

    return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out
