def gidyq_aa_calculator(user_res: list[int]) -> dict[str, str | float]:
    """
    GIDYQ-AA calculator

    Referenced from: https://thomasingenderland.com/2016/11/08/gender-dysphoria-diagnosis-part-5-gidyq-aa-full-text/
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
        if i in [1, 13, 27]:
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
