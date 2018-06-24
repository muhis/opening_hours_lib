"""
Tools for parsing and handling opening hours periods
"""
import calendar
import json
from datetime import datetime
from typing import Dict, List, Tuple


def full_example_dict() ->Dict:
    with open("parsing_tools/full_example.json") as json_file:
        data = json.load(json_file)
    return data


def flatten_dict(opening_hours: Dict) -> List:
    periods_list = []  # type: List[Dict]
    for day, value in opening_hours.items():
        if not value:
            continue
        for item in value:
            item.update({'day': day})
        periods_list += value
    return periods_list


def parse_periods(flat_dicts: List[Dict]) ->List:
    periods = []  # type: List[Tuple[Dict, Dict]]
    for index in range(0, len(flat_dicts) - 1, 2):
        period = (flat_dicts[index], flat_dicts[index + 1])
        periods.append(period)
    return periods


def prettify_time(epoch_time: float) -> str:
    time_object = datetime.utcfromtimestamp(epoch_time)
    return time_object.strftime('%I %p').lstrip('0')


def prettify_periods(periods: List[Tuple]) -> Dict:
    temp_dict = {}  # type: Dict[str, str]
    result = {}  # type: Dict[str, str]
    for period in periods:
        opening, closing = period
        opening_time = prettify_time(opening['value'])
        closing_time = prettify_time(closing['value'])
        day = opening['day']
        if not temp_dict.get(day):
            temp_dict.update({day: f'{opening_time} - {closing_time}'})
        else:
            temp_dict[day] += f', {opening_time} - {closing_time}'
    for day in calendar.day_name:
        result[day.lower()] = temp_dict.get(day.lower(), 'Closed')
    return result


def parse(json: Dict) ->Dict:
    flatten_dicts = flatten_dict(json)
    parsed_periods = parse_periods(flatten_dicts)
    pretty_periods = prettify_periods(parsed_periods)
    return pretty_periods


def stringify_parsed_json(pretty_dict: Dict) ->str:
    output = 'A resturant is open:\n'
    for day, opening_hours in pretty_dict.items():
        output += f'{day.title()}: {opening_hours}\n'
    return output


if __name__ == '__main__':
    example_json = full_example_dict()
    print(stringify_parsed_json(parse(example_json)))

