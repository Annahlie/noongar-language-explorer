import re


# ---------------------------------------------------------
# Application-defined keyword groups
# ---------------------------------------------------------
#
# These categories are used only to explore the English
# meanings in the published dataset.
#
# They are NOT official Noongar linguistic or cultural
# categories.

CATEGORY_KEYWORDS = {
    "Animals": [
        "animal",
        "bird",
        "dog",
        "kangaroo",
        "possum",
        "quokka",
        "quoka",
        "wallaby",
        "emu",
        "fish",
        "snake",
        "insect",
        "seal",
        "sheep",
        "whale",
        "eagle",
        "salmon",
        "curlew",
        "feather",
        "feathers",
    ],

    "Plants and Food": [
        "plant",
        "tree",
        "flower",
        "fruit",
        "seed",
        "food",
        "eat",
        "eating",
        "meat",
        "berry",
        "berries",
        "bush",
        "bushes",
        "leaves",
        "carrot",
        "mushroom",
        "toadstool",
        "fungus",
        "cherry",
        "peach",
        "onion",
        "parsnip",
        "grass",
        "potatoes",
        "bulb",
        "vines",
    ],

    "People and Family": [
        "person",
        "people",
        "man",
        "woman",
        "child",
        "boy",
        "girl",
        "mother",
        "father",
        "brother",
        "sister",
        "family",
        "grandparent",
        "ancestor",
        "uncle",
        "nephew",
        "sweetheart",
    ],

    "Body": [
        "body",
        "head",
        "hand",
        "foot",
        "leg",
        "arm",
        "eye",
        "ear",
        "mouth",
        "nose",
        "skin",
        "breast",
        "tongue",
        "thigh",
        "heart",
        "face",
        "tail",
        "stomach",
        "bone",
        "vein",
        "sinew",
    ],

    "Actions": [
        "bite",
        "biting",
        "hit",
        "strike",
        "striking",
        "put",
        "putting",
        "fight",
        "fighting",
        "grab",
        "grabbing",
        "walk",
        "walking",
        "run",
        "running",
        "jump",
        "jumping",
        "sit",
        "sitting",
        "stand",
        "standing",
        "go",
        "going",
        "come",
        "coming",
        "speak",
        "speaking",
        "climb",
        "climbing",
        "chase",
        "chasing",
        "follow",
        "following",
        "pursuing",
        "see",
        "look",
        "seeing",
        "looking",
        "laugh",
        "laughing",
        "gather",
        "carry",
        "carrying",
        "sing",
        "singing",
        "dance",
        "dancing",
        "throw",
        "throwing",
        "wait",
        "stop",
        "sleep",
        "hunt",
        "hunting",
        "search",
        "searching",
        "track",
        "playing",
        "kill",
        "creep",
        "sneak",
        "creeping",
        "sneaking",
        "hanging",
        "crying",
        "twisting",
        "give",
        "giving",
        "hear",
        "understand",
    ],

    "Nature and Environment": [
        "water",
        "river",
        "ocean",
        "sea",
        "rain",
        "wind",
        "fire",
        "sun",
        "moon",
        "sky",
        "earth",
        "ground",
        "sand",
        "country",
        "peak",
        "rock",
        "cloudy",
        "thunder",
        "waterhole",
    ],

    "Places and Position": [
        "afar",
        "far away",
        "over there",
        "distant",
        "next to",
        "close",
        "inside",
        "home",
        "before",
        "in front of",
        "beside",
        "below",
        "beneath",
        "down",
        "away",
        "that side",
        "high",
        "up high",
        "this side",
    ],

    "Time": [
        "tomorrow",
        "later",
        "by-and-by",
        "forever",
        "always",
        "long ago",
        "before",
        "after",
        "now",
    ],

    "Objects and Shelter": [
        "waddy",
        "firestick",
        "boomerang",
        "spear",
        "hut",
        "camp",
    ],

    "Descriptions and States": [
        "hidden",
        "vanished",
        "exposed",
        "dry",
        "unmarried",
        "unbetrothed",
        "quiet",
        "angry",
        "hot",
        "wet",
        "hungry",
        "weak",
        "big",
        "skinny",
        "thin",
        "good",
        "pretty",
        "ill",
        "strong",
        "dead",
        "beautiful",
        "cold",
        "bad",
        "afraid",
        "different",
        "pitiful",
        "vacant",
        "long",
        "tall",
        "slender",
        "wiry",
    ],
}


# ---------------------------------------------------------
# Explicit overrides for ambiguous meanings
# ---------------------------------------------------------
#
# Some English descriptions contain words that would cause
# a technically correct keyword match but do not represent
# the main meaning of the entry.
#
# These overrides are based only on the published English
# descriptions and decisions made for this application's
# analysis.

CATEGORY_OVERRIDES = {
    "kangaroo berries": ["Plants and Food"],

    "sweat": ["Other"],

    "feathers": ["Animals"],

    "spirit creature/little man": ["Other"],

    "beneath": ["Places and Position"],

    "many (emphatically)": ["Other"],

    "frenchman's peak": ["Nature and Environment"],

    "earth, sand, country": ["Nature and Environment"],

    "hear, understand": ["Actions"],

    "seal (lit. 'dog his head')": ["Animals"],

    "firestick (lit. fire-leg)": ["Objects and Shelter"],

    "very sweet to ear when ripe, grows on the ground of prickly bushes":
        ["Plants and Food"],

    "hunt, search, track": ["Actions"],

    "searching": ["Actions"],
}


def normalise_meaning(text):
    """
    Prepare an English meaning for analysis.
    """

    if not isinstance(text, str):
        return ""

    return text.strip().lower()


def contains_keyword(meaning, keyword):
    """
    Check whether a complete keyword or phrase occurs
    inside an English meaning.

    Word boundaries prevent accidental matches such as:
    'eat' inside 'sweat'
    'man' inside 'many'
    'ear' inside 'earth'
    """

    pattern = r"\b" + re.escape(keyword) + r"\b"

    return re.search(pattern, meaning) is not None


def find_categories(english_meaning):
    """
    Find the application-defined categories associated
    with an English meaning.

    Explicit overrides are checked first.

    If no category matches, the entry is placed in Other.
    """

    meaning = normalise_meaning(english_meaning)

    if meaning == "":
        return ["Other"]

    # -----------------------------------------------------
    # Check explicit overrides first
    # -----------------------------------------------------
    if meaning in CATEGORY_OVERRIDES:
        return CATEGORY_OVERRIDES[meaning]

    matched_categories = []

    # -----------------------------------------------------
    # Check normal keyword groups
    # -----------------------------------------------------
    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            if contains_keyword(meaning, keyword):
                matched_categories.append(category)

                # One match is enough to assign this category
                break

    # -----------------------------------------------------
    # If nothing matched, classify it as Other
    # -----------------------------------------------------
    if len(matched_categories) == 0:
        return ["Other"]

    return matched_categories


def group_entries(data):
    """
    Group dataset records according to their published
    English meanings.
    """

    groups = {}

    # Create categories
    for category in CATEGORY_KEYWORDS:
        groups[category] = []

    # Also create an Other category
    groups["Other"] = []

    # Analyse each dataset record
    for _, row in data.iterrows():

        english_meaning = row["english"]

        categories = find_categories(english_meaning)

        for category in categories:
            groups[category].append(row.to_dict())

    return groups


def count_groups(data):
    """
    Count the number of records assigned to each category.
    """

    groups = group_entries(data)

    counts = {}

    for category, entries in groups.items():
        counts[category] = len(entries)

    return counts