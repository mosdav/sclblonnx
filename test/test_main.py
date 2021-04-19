import os
import numpy as np
from onnx import onnx_ml_pb2 as xpb2
from sclblonnx import empty_graph, graph_from_file, graph_to_file, run


def test_empty_graph():
    g = empty_graph()
    assert type(g) is xpb2.GraphProto, "Failed to create empty graph."


def test_graph_from_file():
    g = graph_from_file("files/non-existing-file.onnx")
    assert not g, "Graph from file failed to check emtpy file."
    g = graph_from_file("files/example01.onnx")
    assert type(g) is xpb2.GraphProto, "Graph from file failed to open file."


def test_graph_to_file():
    g = empty_graph()
    check1 = graph_to_file(g, "")
    assert not check1, "Graph to file failed should have failed."
    check2 = graph_to_file(g, "files/test_graph_to_file.onnx")
    assert check2, "Graph to file failed to write file."
    os.remove("files/test_graph_to_file.onnx")


def test_run():
    g = graph_from_file("files/add.onnx")
    example = {"x1": np.array([2]).astype(np.float32), "x2": np.array([5]).astype(np.float32)}
    result = run(g,
                    inputs=example,
                    outputs=["sum"]
                    )
    assert result[0] == 7, "Add output not correct."
    result = run(g, inputs="", outputs="sum")
    assert not result, "Model with this input should not run."


def test_display():
    from onnx import TensorProto
    print(TensorProto.DOUBLE)

    return True  # No test for display


# def test_scblbl_input():
# def test_list_data_types
# def test_list_operators