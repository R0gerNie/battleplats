import json
import random

class BattleUnit:
    def __init__(self, json_data):
        self.class_name = json_data["class"]
        self.unit_id = json_data["unit_id"]
        self.element = json_data["element"]
        self.max_level = json_data["max_level"]
        self.position = json_data["position"].copy()
        self.attributes = json_data["attributes"]
        self.skills = json_data["skills"].copy()  # 保留原始技能数据

        # 初始化参数
        self.level = 1
        self.position = {
            "x": random.randint(0, 4),  # 随机X坐标
            "y": 1.0,  # 默认地面高度
            "z": random.randint(0, 4)  # 随机Z坐标
        }
        self.faction = random.choice(['A', 'B'])
        # 根据等级筛选可用技能
        self._filter_skills_by_level()

    def _filter_skills_by_level(self):
        """内部方法：根据当前等级过滤主被动技能"""
        active_skills = []
        for skill in self.skills["active"]:
            if skill["level"] <= self.level:
                active_skills.append(skill)
        self.skills["active"] = active_skills
        passive_skills = []
        for skill in self.skills["passive"]:
            if skill["level"] <= self.level:
                passive_skills.append(skill)
        self.skills["passive"] = passive_skills

    def display_status(self):
        print(f"=== {self.class_name} ===")
        print(f"Faction: {self.faction}")
        print(f"ID: {self.unit_id}")
        print(f"Element: {', '.join(self.element)}")
        print(f"Level: {self.level}/{self.max_level}")
        print(f"Attributes:")
        print(f"  HP: {self.attributes[self.level - 1]['hp']}")
        print(f"  ATK: {self.attributes[self.level - 1]['atk']}")
        print(f"  DEF: {self.attributes[self.level - 1]['def']}")
        print(f"  SPD: {self.attributes[self.level - 1]['spd']}")
        print(f"  MAG: {self.attributes[self.level - 1]['mag']}")
        print(f"Position: {self.position}")
        print("Skills:")
        print("  Active:", ", ".join([skill["name"] for skill in self.skills["active"]]))
        print("  Passive:", ", ".join([skill["name"] for skill in self.skills["passive"]]))
        print("======================")


# 示例用法：从JSON文件加载单位
def load_unit_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    return BattleUnit(json_data)


# 使用示例
if __name__ == "__main__":
    # 加载并显示4个不同单位
    units = [
        load_unit_from_file("units/lava_beetle.json"),
        load_unit_from_file("units/magnet_scorpion.json"),
        load_unit_from_file("units/ghost_bat.json"),
        load_unit_from_file("units/black_turtle.json")
    ]

    for unit in units:
        unit.display_status()
        print("\n")

