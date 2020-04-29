#!/usr/bin/env python3
from pl_curve import check_columns
import pandas


def test_check_columns_correct():
    '''FIXME: Implement this test
    Tests check_columns correctly checks items summing to 1.0 returns true
    '''
    df = pandas.DataFrame([0.5,0.5])
    assert check_columns(df) is True
    # raise NotImplementedError("Please implement this test")


def test_check_columns_incorrect():
    df = pandas.DataFrame([0.1, 0.8])
    assert check_columns(df) is False
