# Features: 
#  * Additive:
#    * Single Parent [bool]
#    * Guardian [int]
#    * Children count (>= 3 matters) [int]
#    * Best in profession competition [int] (0, 1, 2 for the last 2 years)
#    * Currently applied corporate rewards [int]
#    * Experience [int]
#  * Multiplicative:
#    * Years from last vacation [int]

from enum import Enum
from math import inf
from datetime import datetime


class TourType(Enum):
    CHILD = 0
    FAMILY = 1

    def to_str(self):
        return self.name.lower()


class FeatureType(Enum):
    SINGLE_PARENT = 0,
    GUARDIAN = 1,
    CHILDREN_COUNT = 2,
    BEST_MEMBER = 3,
    REWARDS = 4,
    EXPERIENCE = 5,
    PREV_VACATIONS = 6,
    DISCIPLINARY_SANCTION = 7


FEATURE_NAME_TO_FEATURE_TYPE = {
    "additive": {
        "single_parent": FeatureType.SINGLE_PARENT,
        "guardian": FeatureType.GUARDIAN,
        "children_count": FeatureType.CHILDREN_COUNT,
        "best_member": FeatureType.BEST_MEMBER,
        "rewards": FeatureType.REWARDS,
        "experience": FeatureType.EXPERIENCE,
    },
    "multiplicative": {
        "prev_vacations": FeatureType.PREV_VACATIONS,
        "disciplinary_sanction": FeatureType.DISCIPLINARY_SANCTION
    }
}

FEATURE_TYPE_TO_MAX_VALUE = {
    FeatureType.SINGLE_PARENT: 1,
    FeatureType.GUARDIAN: 3,
    FeatureType.CHILDREN_COUNT: 5,
    FeatureType.BEST_MEMBER: 2,
    FeatureType.REWARDS: 2,
    FeatureType.EXPERIENCE: 10,
}

FEATURE_TYPE_TO_WEIGHT = {feature: 1 / max_value for feature, max_value in FEATURE_TYPE_TO_MAX_VALUE.items()}


def extract_additive_features(personal_info: dict, tour_type: Enum):
    out = {}

    # crop features
    for feature_name in FEATURE_NAME_TO_FEATURE_TYPE["additive"]:
        if feature_name in personal_info:
            out[feature_name] = \
                min(personal_info[feature_name],
                    FEATURE_TYPE_TO_MAX_VALUE[FEATURE_NAME_TO_FEATURE_TYPE["additive"][feature_name]])

    # remove features not used for CHILD
    if tour_type == TourType.CHILD:
        for key in ["best_member", "rewards"]:
            out.pop(key, None)

    return out


def extract_multiplicative_features(personal_info: dict, tour_type: Enum):
    out = {}

    # parse features
    for feature_name in FEATURE_NAME_TO_FEATURE_TYPE["multiplicative"]:
        if feature_name in personal_info and feature_name == "prev_vacations":
            max_date = max(
                [datetime.strptime(vacation["date"], "%Y-%m-%d") for vacation in personal_info[feature_name] if
                 vacation["type"] == tour_type.to_str()])
            out["prev_vacation_years"] = datetime.now().year - max_date.year - \
                                         ((datetime.now().month, datetime.now().day) < (max_date.month, max_date.day))
        if feature_name in personal_info and feature_name == "disciplinary_sanction":
            out["no_disciplinary_sanction"] = abs(1 - personal_info[feature_name])

    return out


def compute_score(personal_info: dict, tour_type: Enum):
    score = 0
    additive_features = extract_additive_features(personal_info, tour_type)
    for feature, val in additive_features.items():
        weight = FEATURE_TYPE_TO_WEIGHT.get(FEATURE_NAME_TO_FEATURE_TYPE["additive"][feature], 0)
        score += weight * val
    score /= len(additive_features)

    multiplicative_features = extract_multiplicative_features(personal_info, tour_type)
    for feature, val in multiplicative_features.items():
        weight = 1
        score *= weight * val

    return score
