'''
Description: 
Version: 1.0
Autor: Wenjun Zhuang
Date: 2022-09-28 14:11:50
LastEditors: Wenjun Zhuang
LastEditTime: 2022-10-06 14:34:06
'''
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from collections import defaultdict


class ConfigReader:
    '''
    ConfigReader基类
    '''
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.config_dict = {}

    def read_from_file(self) -> None:
        '''
        根据文件路径读入json
        '''
        try:
            with open(self.filepath) as f:
                config_json = json.load(f)
        except FileNotFoundError:
            raise Exception(f'This {self.filepath} is not found')
        except json.decoder.JSONDecodeError:
            raise Exception(f'This {self.filepath} cannot be decode by json')
        self.config_dict = config_json
        return

    def validate_key(self) -> None:
        '''
        待子类实现的验证字段
        '''
        return


ROLLOVER_RULE_NAME_PATTERN = '^[A-Za-z0-9_]+.[A-Za-z0-9]+$' # rollover rule的正则表达，<string>.<string>

# json schema 实现字段验证
substrategy_schema = {
    "type": "object",
    "required": ["is_activated", "rollover_rules", "hist_data_freq", "timing"],
    "properties": {
        "is_activated": {"type": "boolean"},
        "rollover_rules": {"type": "array",
                           "items": {"type": "string",
                                     "pattern": ROLLOVER_RULE_NAME_PATTERN}},
        "hist_data_freq": {"type": "string"},
        "timing": {
            "type": "object",
            "required": ["order_time", "fill_time"],
            "properties": {
                "order_time": {"type": "string"},
                "fill_time": {"type": "string"}
            }
        }
    }
}


class SubstrategyConfigReader(ConfigReader):
    '''
    子策略ConfigReader
    新建实例后即可直接调用属性
    config_dict: dict 
        读入的json配置字典
    strategy_list: list 
        子策略列表
    all_rollover_rules: dict 
        rollover的类型字典
    rollover_rules_timing: dict 
        rollover对应的timing字典
    order_time_rules: dict 
        order time对应的子策略字典
    '''
    def __init__(self, filepath) -> None:
        super().__init__(filepath)
        self.strategy_list = []
        self.all_rollover_rules = defaultdict(set)
        self.rollover_rules_timing = defaultdict(lambda: {"order_time": set(), "fill_time": set()})
        self.order_time_rules = defaultdict(set)
        self.read_from_file()
        self.validate_key()
        self.sort_attributes()

    def validate_key(self) -> None:
        '''
        重写了字段验证以及字段提取
        '''
        try:
            for strategy_name, strategy_config in self.config_dict.items():
                validate(instance=strategy_config, schema=substrategy_schema)
                self.strategy_list.append(strategy_name)
                rollover_rules = strategy_config["rollover_rules"]
                order_time = strategy_config['timing']['order_time']
                fill_time = strategy_config['timing']['fill_time']
                for rr in rollover_rules:
                    rr_name, rr_type = rr.split('.')
                    self.all_rollover_rules[rr_name].add(rr_type)
                    self.rollover_rules_timing[rr_name]['order_time'].add(order_time)
                    self.rollover_rules_timing[rr_name]['fill_time'].add(fill_time)
                    self.order_time_rules[order_time].add(strategy_name)
        except ValidationError as e:
            raise Exception(f'Rollover rule does not match pattern\n' + e.message)
        return

    def sort_attributes(self) -> None:
        '''
        整理字段
        '''
        for key, value in self.all_rollover_rules.items():
            self.all_rollover_rules[key] = sorted(list(value))
        for rr in self.rollover_rules_timing.keys():
            self.rollover_rules_timing[rr]['order_time'] = sorted(list(self.rollover_rules_timing[rr]['order_time']))
            self.rollover_rules_timing[rr]['fill_time'] = sorted(list(self.rollover_rules_timing[rr]['fill_time']))
        for key, value in self.order_time_rules.items():
            self.order_time_rules[key] = sorted(list(value))


if __name__ == "__main__":
    scr = SubstrategyConfigReader('substrategy_config.json')
    print(scr.config_dict)
    print(scr.strategy_list)
    print(scr.all_rollover_rules)
    print(scr.rollover_rules_timing)
    print(scr.order_time_rules)