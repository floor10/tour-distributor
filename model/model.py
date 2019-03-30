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


class TourType(Enum):
    CHILD_CAMP=0
    HEALING=1

class FeatureType(Enum):
    SINGLE_PARENT=0,
    GUARDIAN=1,
    CHILDREN_COUNT=2,
    BEST_MEMBER=3,
    REWARDS=4,
    EXPERIENCE=5,
    YEARS_FROM_LAST_TOUR=6

FEATURE_NAME_TO_FEATURE_TYPE = {
    "single_parent": FeatureType.SINGLE_PARENT,
    "guardian": FeatureType.GUARDIAN,
    "children_count": FeatureType.CHILDREN_COUNT,
    "best_member": FeatureType.BEST_MEMBER,
    "rewards": FeatureType.REWARDS,
    "experience": FeatureType.EXPERIENCE
}

FEATURE_TYPE_TO_MAX_VALUE = {
    FeatureType.SINGLE_PARENT: 1,
    FeatureType.GUARDIAN: 3,
    FeatureType.CHILDREN_COUNT: 5,
    FeatureType.BEST_MEMBER: 2,
    FeatureType.REWARDS: 2,
    FeatureType.EXPERIENCE: 10
}

FEATURE_TYPE_TO_WEIGHT = {feature: 1 / max_value for feature, max_value in FEATURE_TYPE_TO_MAX_VALUE.items()}


def extract_cropped_features(personal_info: dict, tour_type: Enum):
    out = {}
    for feature_name in FEATURE_NAME_TO_FEATURE_TYPE:
        if feature_name in personal_info:
            out[feature_name] = \
                min(personal_info[feature_name], FEATURE_TYPE_TO_MAX_VALUE[FEATURE_NAME_TO_FEATURE_TYPE[feature_name]])

    if tour_type == TourType.CHILD_CAMP:
        for key in ["best_member", "rewards"]:
            out.pop(key, None)

    return out


def compute_score(personal_info: dict, tour_type: Enum):
    score = 0
    features = extract_cropped_features(personal_info, tour_type)
    for feature, val in features.items():
        weight = FEATURE_TYPE_TO_WEIGHT[FEATURE_NAME_TO_FEATURE_TYPE[feature]]
        score += weight * val
    score /= len(features)

    # TODO: support multiplication feature (years from last tour of current type)

