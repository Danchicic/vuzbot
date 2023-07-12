from dataclasses import dataclass
from typing import TypedDict


class MainStructure(TypedDict):
    snils: str
    priority: int
    mark: str


@dataclass
class StructureForBot:
    students: MainStructure
    sorted_students: MainStructure
    budget: str


class Compets(TypedDict):
    hrefs: list
    name: list


@dataclass
class Competitions:
    competitions: Compets
