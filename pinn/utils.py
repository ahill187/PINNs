from __future__ import annotations
import pathlib
import os
import importlib.resources as pkg_resources


PINN_PATH = pathlib.Path(__file__).parents[1].absolute()


def get_data_path(data_path: str | pathlib.Path) -> pathlib.Path:
    """Get the full path to a data file or folder in the ``PINN`` package.

    Args:
        data_path: The path to the file or folder.

    Returns:
        The full path to the file or folder.
    """

    data_path = pathlib.Path(data_path)
    if data_path.parts[0] == "tests":
        data_folder = "tests.data"
        data_path = data_path.relative_to("tests/data")
    elif data_path.parts[0] == "data":
        data_folder = "pinn.data"
        data_path = data_path.relative_to("data")
  
    package_path = str(pkg_resources.files(data_folder).joinpath(str(data_path)))

    if os.path.isfile(package_path) or os.path.isdir(package_path):
        return pathlib.Path(package_path)
    else:
        raise FileNotFoundError(f"Path {data_path} not found.")














