def gidyq_aa_calculator(user_res: list[int]) -> dict[str, str | float]:
    """
    GIDYQ-AA calculator

    Reference-1: https://thomasingenderland.com/2016/11/08/gender-dysphoria-diagnosis-part-5-gidyq-aa-full-text/
    """
    scale_result: dict[str, str | float] = {}

    # Counting choices
    total_choices = 0
    choice_count: dict[str, int] = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
    }
    for i in range(len(user_res)):
        if user_res[i] == 0:
            continue
        total_choices += 1
        if (i + 1) in [1, 13, 27]:
            # Reversed Scoring
            choice_count[str(6 - user_res[i])] += 1
        else:
            choice_count[str(user_res[i])] += 1

    # Finding multiplied totals
    multiplied_totals: dict[str, int] = {
        "1": choice_count["1"] * 1,
        "2": choice_count["2"] * 2,
        "3": choice_count["3"] * 3,
        "4": choice_count["4"] * 4,
        "5": choice_count["5"] * 5,
    }

    # Finding raw score
    raw_score = sum(multiplied_totals.values())

    # generating scale_result
    scale_result["score"] = round(raw_score / total_choices, 2)
    scale_result["result type"] = 'text'

    if scale_result["score"] <= 3.0:
        scale_result["result"] = 'Scale score is strongly suggestive of gender dysphoria.'
    else:
        scale_result["result"] = 'Scale score reflects absence of gender dysphoria.'

    return scale_result


def dass_y_calculator(user_res: list[int]) -> dict[str, str | float | dict[str, list[str | float]]]:
    """
    DASS-Y calculator

    Reference-1: https://novopsych.com.au/assessments/child/depression-anxiety-stress-scale-youth-version-dass-y/
    Reference-2: https://www2.psy.unsw.edu.au/dass//DASS-Y%20cutoffs.htm
    """
    scale_result: dict[str, str | float | dict[str, list[str | float]]] = {}

    # Counting scores
    scores_count: dict[str, int] = {
        "total": 0,
        "depression": 0,
        "anxiety": 0,
        "stress": 0,
    }
    for i in range(len(user_res)):
        if user_res[i] not in range(0, 4):
            raise ValueError
        scores_count["total"] += user_res[i]
        if (i + 1) in [3, 5, 10, 13, 16, 17, 21]:
            scores_count["depression"] += user_res[i]
        elif (i + 1) in [2, 4, 7, 9, 15, 19, 20]:
            scores_count["anxiety"] += user_res[i]
        elif (i + 1) in [1, 6, 8, 11, 12, 14, 18]:
            scores_count["stress"] += user_res[i]

    # generating scale_result
    scale_result["score"] = scores_count["total"]
    scale_result["result type"] = 'map<parameter_name_text, list[parameter_result_text, parameter_percentile_float]>'
    scale_result["result"] = {
        "total": ["", round((scores_count["total"] / 63) * 100, 2)],
        "depression": ["", round((scores_count["depression"] / 21) * 100, 2)],
        "anxiety": ["", round((scores_count["anxiety"] / 21) * 100, 2)],
        "stress": ["", round((scores_count["stress"] / 21) * 100, 2)],
    }

    # parameter == total
    if scores_count["total"] in range(0, 24):
        scale_result["result"]["total"][0] = "Normal"
    elif scores_count["total"] in range(24, 30):
        scale_result["result"]["total"][0] = "Mild"
    elif scores_count["total"] in range(30, 40):
        scale_result["result"]["total"][0] = "Moderate"
    elif scores_count["total"] in range(40, 47):
        scale_result["result"]["total"][0] = "Severe"
    else:
        scale_result["result"]["total"][0] = "Extremely Severe"

    # parameter == depression
    if scores_count["depression"] in range(0, 7):
        scale_result["result"]["depression"][0] = "Normal"
    elif scores_count["depression"] in range(7, 9):
        scale_result["result"]["depression"][0] = "Mild"
    elif scores_count["depression"] in range(9, 14):
        scale_result["result"]["depression"][0] = "Moderate"
    elif scores_count["depression"] in range(14, 17):
        scale_result["result"]["depression"][0] = "Severe"
    else:
        scale_result["result"]["depression"][0] = "Extremely Severe"

    # parameter == anxiety
    if scores_count["anxiety"] in range(0, 6):
        scale_result["result"]["anxiety"][0] = "Normal"
    elif scores_count["anxiety"] in range(6, 8):
        scale_result["result"]["anxiety"][0] = "Mild"
    elif scores_count["anxiety"] in range(8, 13):
        scale_result["result"]["anxiety"][0] = "Moderate"
    elif scores_count["anxiety"] in range(13, 16):
        scale_result["result"]["anxiety"][0] = "Severe"
    else:
        scale_result["result"]["anxiety"][0] = "Extremely Severe"

    # parameter == stress
    if scores_count["stress"] in range(0, 12):
        scale_result["result"]["stress"][0] = "Normal"
    elif scores_count["stress"] in range(12, 14):
        scale_result["result"]["stress"][0] = "Mild"
    elif scores_count["stress"] in range(14, 17):
        scale_result["result"]["stress"][0] = "Moderate"
    elif scores_count["stress"] in range(17, 19):
        scale_result["result"]["stress"][0] = "Severe"
    else:
        scale_result["result"]["stress"][0] = "Extremely Severe"

    return scale_result


def overt_aggresion_calculator(user_res: list[int]) -> dict[str, str | float]:
    """
    overt-aggresion calculator

    Reference-1: https://www.psytoolkit.org/survey-library/aggression-adolescents.html
    """
    scale_result: dict[str, str | float] = {}

    # Counting score
    aggressionscore = 0
    for i in user_res:
        assert i <= 6 and i >= 0, "Invalid choice number in user_res"
        aggressionscore += i

    # generating scale_result
    scale_result["score"] = aggressionscore
    scale_result["result type"] = 'text'
    scale_result["result"] = f'''\
Your aggression score is {aggressionscore} on a range from 0 to 66.<br>
In the original study developing the scale, the following averages were found:
Boys: 19.3
Girls: 13.2'''

    return scale_result
