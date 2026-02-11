import pytest
from Calc_Python.metric import bmi_metric
from Calc_Python.imperial import bmi_imperial

def test_bmi_metric_normal(monkeypatch, capsys):
    # Arrange
    inputs = iter(["70", "175"]) 
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    bmi_metric()
    captured = capsys.readouterr()

    # Assert
    assert "BMI:" in captured.out
    assert "22.86" in captured.out
    assert "Normal weight" in captured.out

def test_bmi_metric_underweight(monkeypatch, capsys):
    # Arrange
    inputs = iter(["45", "170"])  
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    bmi_metric()
    captured = capsys.readouterr()

    # Assert
    assert "Underweight" in captured.out

def test_bmi_metric_overweight_boundary(monkeypatch, capsys):
    # Arrange
    inputs = iter(["77", "175"])  
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    bmi_metric()
    captured = capsys.readouterr()

    # Assert
    assert "Overweight" in captured.out

def test_bmi_imperial_normal(monkeypatch, capsys):
    # Arrange
    inputs = iter(["154", "69"]) 
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    bmi_imperial()
    captured = capsys.readouterr()

    # Assert
    assert "Your bmi is:" in captured.out
    assert "Normal weight" in captured.out

def test_bmi_imperial_obese(monkeypatch, capsys):
    # Arrange
    inputs = iter(["250", "65"])  
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Act
    bmi_imperial()
    captured = capsys.readouterr()

    # Assert
    assert "Obese Class" in captured.out
