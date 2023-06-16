AGGRESSION = 0
ANXIETY = 1
DEPRESSION = 2
SOCIAL_PHOBIA = 3
LOW_ESTEEM = 4

GENTLE = 0
CONFIDENCE = 1
HAPPINESS = 2
SOCIAL_COMPETENCE = 3
HIGH_ESTEEM = 4

class Character():
    def __init__(self, index, combination, name, description):
        self.index = index
        self.combination = combination
        self.name = name
        self.description = description
    
CHARACTER_LIST = []
CHARACTER_LIST.append(Character(0, (AGGRESSION, CONFIDENCE), "공격적인 돼지바 프라푸치노", "약간 공격적이면서 자신감 넘치는 너!"))
CHARACTER_LIST.append(Character(1, (AGGRESSION, HAPPINESS), "노른자가 두개 띄워진 쌍화탕", "다른 사람에게는 공격적이지만 내면은 행복한 너!"))
CHARACTER_LIST.append(Character(2, (AGGRESSION, SOCIAL_COMPETENCE), "샷 6번 추가한 공격적인 아메리카노", "공격적이지만 사회성이 높은 너!"))
CHARACTER_LIST.append(Character(3, (AGGRESSION, HIGH_ESTEEM), "자존감 높은 1리터 쌍화탕", "공격적이지만 자존감은 높은 너!"))
CHARACTER_LIST.append(Character(4, (ANXIETY, GENTLE), "샷 6번 추가한 따뜻한 라떼", "혼자있기를 좋아하는 온화한 당신"))
CHARACTER_LIST.append(Character(5, (ANXIETY, HAPPINESS), "혼자 있기 좋아하는 자몽 허니 블랙티", "혼자있기를 좋아하는 당신"))
CHARACTER_LIST.append(Character(6, (ANXIETY, SOCIAL_COMPETENCE), "따뜻한 아이스 아메리카노", "혼자있고 싶지만 인기는 많은 당신"))
CHARACTER_LIST.append(Character(7, (ANXIETY, HIGH_ESTEEM), "안정이 필요한 민트 초코 라떼", "혼자있기를 좋아하고 자존감은 높은 당신"))
CHARACTER_LIST.append(Character(8, (DEPRESSION, GENTLE), "미지근한 카모마일티", "가끔 우울하지만 온화한 성격의 당신"))
CHARACTER_LIST.append(Character(9, (DEPRESSION, CONFIDENCE), "자신감이 넘치는 유니콘 프라푸치노", "가끔 우울하지만 자신감 넘치는 당신"))
CHARACTER_LIST.append(Character(10, (DEPRESSION, SOCIAL_COMPETENCE), "얼음이 녹아버린 아샷추", "무기력한 인싸"))
CHARACTER_LIST.append(Character(11, (DEPRESSION, HIGH_ESTEEM), "톡 쏘는 블루레몬에이드", "무기력하고 자존감 높은 당신"))
CHARACTER_LIST.append(Character(12, (SOCIAL_PHOBIA, GENTLE), "휘핑 가득 따뜻한 민트초코라떼", "많은 사람들과 섞이기 어려워하는 온화한 친구"))
CHARACTER_LIST.append(Character(13, (SOCIAL_PHOBIA, CONFIDENCE), "펄 추가 아이스아메리카노", "많은 사람들과 섞이기 어려워하는 자신감 넘치는 친구"))
CHARACTER_LIST.append(Character(14, (SOCIAL_PHOBIA, HAPPINESS), "행복한 민트초코프라푸치노", "많은 사람들과 섞이기 어려워하지만 행복한 친구"))
CHARACTER_LIST.append(Character(15, (SOCIAL_PHOBIA, HIGH_ESTEEM), "혼자가 된 제주 유기농 감귤 주스", "많은 사람들과 섞이기 어려워하는 높은 자존감의 친구"))
CHARACTER_LIST.append(Character(16, (LOW_ESTEEM, GENTLE), "거품 뺀 카푸치노", "자존감이 낮고 온화한 당신"))
CHARACTER_LIST.append(Character(17, (LOW_ESTEEM, CONFIDENCE), "초코쉐이크가 되고싶은 밀크쉐이크", "자존감이 낮고 자신감이 높은 당신"))
CHARACTER_LIST.append(Character(18, (LOW_ESTEEM, HAPPINESS), "따뜻한 숏라떼", "자존감이 낮고 행복한 당신"))
CHARACTER_LIST.append(Character(19, (LOW_ESTEEM, SOCIAL_COMPETENCE), "수줍은 복숭아 아이스티", "자존감이 낮고 활발한 당신"))

import random

def match_character(score):
    bad_index = score.index(max(score))
    good_index = score.index(min(score))
    
    if bad_index == good_index:
        numbers = list(range(5))
        random.shuffle(numbers)
        bad_index, good_index = numbers[:2]
        
    combination = (bad_index, good_index)
    
    for character in CHARACTER_LIST:
        if character.combination == combination:
            return character.index
    
    return -1