# Generate diff:
[![Actions Status](https://github.com/timvildanov/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/timvildanov/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/2b26206b2d19bc04ccb0/maintainability)](https://codeclimate.com/github/timvildanov/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/2b26206b2d19bc04ccb0/test_coverage)](https://codeclimate.com/github/timvildanov/python-project-50/test_coverage)

## Описание проекта:

Учебный проект в рамках онлайн школы программирования Хекслет (https://ru.hexlet.io/)

Программа производит сравнение двух файлов в формате json или yaml.
Результат выводится как опция в формате json, в виде дерева или в виде текстовой записи. 

## Функции проекта

Версия python = 3.10
Версия pyaaml = 6.0.1

Программа поддерживает форматы: текст, YAML, JSON

Демонстрация работы программы: 

### Вызов справки по работе с программой
```
gendiff -h
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
```
