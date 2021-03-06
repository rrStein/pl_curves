#!/usr/bin/env python3
import pytest
from pl_curve import run
import pandas
import os


def test_run():

    f = open("test-input.tsv", "w")
    f.write("Bin\tStep I\tStep II\n")
    f.write("219\t0.5\t0.3\n")
    f.write("218\t0.5\t0.7\n")
    f.close()

    # delete test.png if it already exists
    try:
        os.remove("test.tsv")
    # catch the error if file doesn't exist
    except FileNotFoundError as error:
        pass

    # delete test.png if it already exists
    try:
        os.remove("test.png")
    # catch the error if file doesn't exist
    except FileNotFoundError as error:
        pass

    run("test-input.tsv", "test.png", "test.tsv")
    assert os.path.isfile("test.tsv") is True
    assert os.path.isfile("test.png") is True

    data = pandas.read_csv("test.tsv", delimiter='\t', index_col=0)
    assert data.loc['Step I', 'Gini'] == 0.0
    assert data.loc['Step I', 'Corrected Gini'] == 0.0
    assert data.loc['Step II', 'Gini'] == 0.2
    assert data.loc['Step II', 'Corrected Gini'] == 0.4
    
def test_run_fail():
    f = open("test-input.tsv", "w")
    f.write("Bin\tStep I\tStep II\n")
    f.write("219\t0.8\t0.3\n")
    f.write("218\t0.5\t0.7\n")
    f.close()

    # delete test.png if it already exists
    try:
        os.remove("test.tsv")
    # catch the error if file doesn't exist
    except FileNotFoundError as error:
        pass

    # delete test.png if it already exists
    try:
        os.remove("test.png")
    # catch the error if file doesn't exist
    except FileNotFoundError as error:
        pass

    
    # 
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run("test-input.tsv", "test.png", "test.tsv")
        
        # captured = capsys.readouterr()
        # errMsg = "Error: columns don't sum to 1\n"
        # assert captured == errMsg
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
    
    
