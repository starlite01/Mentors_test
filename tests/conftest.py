from pytest import fixture

from src.task import CustomDict


@fixture(scope="function")
def custom_dict() -> CustomDict:
    return CustomDict()
