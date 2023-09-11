from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import helpers

# Create your views here.


@api_view(["GET"])
def scales(request):
    return Response({
        'success': 1,
        'All scale names': [
            "Gender Dysphoria Scale (Female Assigned at Birth)",
            "Gender Dysphoria Scale (Male Assigned at Birth)",
            "Depression Anxiety Stress Scales - Youth Version",
        ],
        'Gender Dysphoria Scale (Female Assigned at Birth)': {
            'name': "GIDYQ-AA",
            'link': "gidyq-aa-female",
        },
        'Gender Dysphoria Scale (Male Assigned at Birth)': {
            'name': "GIDYQ-AA",
            'link': "gidyq-aa-male",
        },
        'Depression Anxiety Stress Scales - Youth Version': {
            'name': "DASS-Y",
            'link': "dass-y",
        },
    })


@api_view(["GET"])
def gidyq_aa_female(request):
    USER_RES = request.GET.get('user_res')

    if USER_RES == None or USER_RES.strip() == '':
        return Response({
            'success': 1,
            'pretext': None,
            'questions': [
                "In the past 12 months, have you felt satisfied being a woman?",
                "In the past 12 months, have you felt uncertain about your gender, that is, feeling somewhere in between a woman and a man?",
                "In the past 12 months, have you felt pressured by others to be a woman, although you don't really feel like one?",
                "In the past 12 months, have you felt, unlike most women, that you have to work at being a woman?",
                "In the past 12 months, have you felt that you were not a real woman?",
                "In the past 12 months, have you felt, given who you really are (e.g., what you like to do, how you act with other people), that it would be better for you to live as a man rather than as a woman?",
                "In the past 12 months, have you had dreams? If NO, skip to Question 8. If YES, Have you been in your dreams? If NO, skip to Question 8. If YES, In the past 12 months, have you had dreams in which you were a man?",
                "In the past 12 months, have you felt unhappy about being a woman?",
                "In the past 12 months, have you felt uncertain about yourself, at times feeling more like a man and at times feeling more like a woman?",
                "In the past 12 months, have you felt more like a man than like a woman?",
                "In the past 12 months, have you felt that you did not have anything in common with either men or women?",
                "In the past 12 months, have you been bothered by seeing yourself identified as female or having to check the box “F” for female on official forms (e.g., employment applications, driver's license, passport)?",
                "In the past 12 months, have you felt comfortable when using women's restrooms in public places?",
                "In the past 12 months, have strangers treated you as a man?",
                "In the past 12 months, at home, have people you know, such as friends or relatives, treated you as a man?",
                "In the past 12 months, have you had the wish or desire to be a man?",
                "In the past 12 months, at home, have you dressed and acted as a man?",
                "In the past 12 months, at parties or at other social gatherings, have you presented yourself as a man?",
                "In the past 12 months, at work or at school, have you presented yourself as a man?",
                "In the past 12 months, have you disliked your body because it is female (e.g., having breasts or having a vagina)?",
                "In the past 12 months, have you wished to have hormone treatment to change your body into a man's?",
                "In the past 12 months, have you wished to have an operation to change your body into a man's (e.g., to have your breasts removed or to have a penis made)?",
                "In the past 12 months, have you made an effort to change your legal sex (e.g., on a driver's licence or credit card)?",
                "In the past 12 months, have you thought of yourself as a “hermaphrodite” or an “intersex” rather than as a man or woman?",
                "In the past 12 months, have you thought of yourself as a “transgendered person”?",
                "In the past 12 months, have you thought of yourself as a man?",
                "In the past 12 months, have you thought of yourself as a woman?",
            ],
            'choices': ["always", "often", "sometimes", "rarely", "never"],
            'skippable': True,
        })

    try:
        USER_RES_LIST = [int(_) for _ in USER_RES.split(',')]
    except ValueError or TypeError:
        return Response({
            'success': 0,
            'msg': "Incorrect user_res, user_res must be intergers separated by commas (no spaces, alphabets, etc.)",
        })

    try:
        SCALE_RESULT = helpers.gidyq_aa_calculator(USER_RES_LIST)
    except:
        return Response({
            'success': 0,
            'msg': 'Unknown Exception Occurred!',
        })

    return Response({
        'success': 1,
        'score': SCALE_RESULT.get('score'),
        'result type': SCALE_RESULT.get('result type'),
        'result': SCALE_RESULT.get('result'),
        'refrences': [
            "Deogracias JJ, Johnson LL, Meyer-Bahlburg HF, Kessler SJ, Schober JM, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults. J Sex Res. 2007 Nov;44(4):370-9. doi: 10.1080/00224490701586730. PMID: 18321016.",
            "Singh D, Deogracias JJ, Johnson LL, Bradley SJ, Kibblewhite SJ, Owen-Anderson A, Peterson-Badali M, Meyer-Bahlburg HF, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults: further validity evidence. J Sex Res. 2010 Jan;47(1):49-58. doi: 10.1080/00224490902898728. PMID: 19396705.",
        ],
    })


@api_view(["GET"])
def gidyq_aa_male(request):
    USER_RES = request.GET.get('user_res')

    if USER_RES == None or USER_RES.strip() == '':
        return Response({
            'success': 1,
            'pretext': None,
            'questions': [
                "In the past 12 months, have you felt satisfied being a man?",
                "In the past 12 months, have you felt uncertain about your gender, that is, feeling somewhere in between a man and a woman?",
                "In the past 12 months, have you felt pressured by others to be a man, although you don't really feel like one?",
                "In the past 12 months, have you felt, unlike most men, that you have to work at being a man?",
                "In the past 12 months, have you felt that you were not a real man?",
                "In the past 12 months, have you felt, given who you really are (e.g., what you like to do, how you act with other people), that it would be better for you to live as a woman rather than as a man?",
                "In the past 12 months, have you had dreams? If NO, skip to Question 8. If YES, Have you been in your dreams? If NO, skip to Question 8. If YES, In the past 12 months, have you had dreams in which you were a woman?",
                "In the past 12 months, have you felt unhappy about being a man?",
                "In the past 12 months, have you felt uncertain about yourself, at times feeling more like a woman and at times feeling more like a man?",
                "In the past 12 months, have you felt more like a woman than like a man?",
                "In the past 12 months, have you felt that you did not have anything in common with either women or men?",
                "In the past 12 months, have you been bothered by seeing yourself identified as male or having to check the box “M” for male on official forms (e.g., employment applications, driver's license, passport)?",
                "In the past 12 months, have you felt comfortable when using men's restrooms in public places?",
                "In the past 12 months, have strangers treated you as a woman?",
                "In the past 12 months, at home, have people you know, such as friends or relatives, treated you as a woman?",
                "In the past 12 months, have you had the wish or desire to be a woman?",
                "In the past 12 months, at home, have you dressed and acted as a woman?",
                "In the past 12 months, at parties or at other social gatherings, have you presented yourself as a woman?",
                "In the past 12 months, at work or at school, have you presented yourself as a woman?",
                "In the past 12 months, have you disliked your body because it is male (e.g., having a penis or having hair on your chest, arms, and legs)?",
                "In the past 12 months, have you wished to have hormone treatment to change your body into a woman's?",
                "In the past 12 months, have you wished to have an operation to change your body into a woman's (e.g., to have your penis removed or to have a vagina made)?",
                "In the past 12 months, have you made an effort to change your legal sex (e.g., on a driver's licence or credit card)?",
                "In the past 12 months, have you thought of yourself as a “hermaphrodite” or an “intersex” rather than as a man or woman?",
                "In the past 12 months, have you thought of yourself as a “transgendered person”?",
                "In the past 12 months, have you thought of yourself as a woman",
                "In the past 12 months, have you thought of yourself as a man?",
            ],
            'choices': ["always", "often", "sometimes", "rarely", "never"],
            'skippable': True,
        })

    try:
        USER_RES_LIST = [int(_) for _ in USER_RES.split(',')]
    except ValueError or TypeError:
        return Response({
            'success': 0,
            'msg': "Incorrect user_res, user_res must be intergers separated by commas (no spaces, alphabets, etc.)",
        })
    except:
        return Response({
            'success': 0,
            'msg': 'Unknown Exception Occurred!',
        })

    try:
        SCALE_RESULT = helpers.gidyq_aa_calculator(USER_RES_LIST)
    except KeyError:
        return Response({
            'success': 0,
            'msg': 'Incorrect user_res, user_res can contain integers only in the inclusive range [0, no_of_choices]',
        })
    except:
        return Response({
            'success': 0,
            'msg': 'Unknown Exception Occurred!',
        })

    return Response({
        'success': 1,
        'score': SCALE_RESULT.get('score'),
        'result type': SCALE_RESULT.get('result type'),
        'result': SCALE_RESULT.get('result'),
        'refrences': [
            "Deogracias JJ, Johnson LL, Meyer-Bahlburg HF, Kessler SJ, Schober JM, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults. J Sex Res. 2007 Nov;44(4):370-9. doi: 10.1080/00224490701586730. PMID: 18321016.",
            "Singh D, Deogracias JJ, Johnson LL, Bradley SJ, Kibblewhite SJ, Owen-Anderson A, Peterson-Badali M, Meyer-Bahlburg HF, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults: further validity evidence. J Sex Res. 2010 Jan;47(1):49-58. doi: 10.1080/00224490902898728. PMID: 19396705.",
        ],
    })


@api_view(["GET"])
def dass_y(request):
    USER_RES = request.GET.get('user_res')

    if USER_RES == None or USER_RES.strip() == '':
        return Response({
            'success': 1,
            'pretext':'We would like to find out how you have been feeling in THE PAST WEEK. There are some sentences below. Please select the statement which best shows how TRUE each sentence was of you during the past week. There are no right or wrong answers.',
            'questions': [
            ],
            'choices': ["Not true", "A little true", "Fairly true", "Very true"],
            'skippable': True,
        })

    try:
        USER_RES_LIST = [int(_) for _ in USER_RES.split(',')]
    except ValueError or TypeError:
        return Response({
            'success': 0,
            'msg': "Incorrect user_res, user_res must be intergers separated by commas (no spaces, alphabets, etc.)",
        })
    except:
        return Response({
            'success': 0,
            'msg': 'Unknown Exception Occurred!',
        })

    try:
        SCALE_RESULT = helpers.gidyq_aa_calculator(USER_RES_LIST)
    except KeyError:
        return Response({
            'success': 0,
            'msg': 'Incorrect user_res, user_res can contain integers only in the inclusive range [0, no_of_choices]',
        })
    except:
        return Response({
            'success': 0,
            'msg': 'Unknown Exception Occurred!',
        })

    return Response({
        'success': 1,
        'score': SCALE_RESULT.get('score'),
        'result type': SCALE_RESULT.get('result type'),
        'result': SCALE_RESULT.get('result'),
        'refrences': [
            "Deogracias JJ, Johnson LL, Meyer-Bahlburg HF, Kessler SJ, Schober JM, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults. J Sex Res. 2007 Nov;44(4):370-9. doi: 10.1080/00224490701586730. PMID: 18321016.",
            "Singh D, Deogracias JJ, Johnson LL, Bradley SJ, Kibblewhite SJ, Owen-Anderson A, Peterson-Badali M, Meyer-Bahlburg HF, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults: further validity evidence. J Sex Res. 2010 Jan;47(1):49-58. doi: 10.1080/00224490902898728. PMID: 19396705.",
        ],
    })
