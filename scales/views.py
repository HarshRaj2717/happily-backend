from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import helpers

# Create your views here.


@api_view(["GET"])
def scales(request):
    return Response({
        "All scale names": [
            "Gender Dysphoria Scale (Female Assigned at Birth)",
        ],
        "Gender Dysphoria Scale (Female Assigned at Birth)": {
            'name': "GIDYQ-AA",
            'link': "gidyq-aa-female",
        },
    })


@api_view(["GET"])
def gidyq_aa_female(request):
    USER_RES = request.GET.get('user_res')

    if USER_RES == None:
        return Response({
            'questions': [
                "01. In the past 12 months, have you felt satisfied being a woman?",
                "02. In the past 12 months, have you felt uncertain about your gender, that is, feeling somewhere in between a woman and a man?",
                "03. In the past 12 months, have you felt pressured by others to be a woman, although you don't really feel like one?",
                "04. In the past 12 months, have you felt, unlike most women, that you have to work at being a woman?",
                "05. In the past 12 months, have you felt that you were not a real woman?",
                "06. In the past 12 months, have you felt, given who you really are (e.g., what you like to do, how you act with other people), that it would be better for you to live as a man rather than as a woman?",
                "07. In the past 12 months, have you had dreams? If NO, skip to Question 8. If YES, Have you been in your dreams? If NO, skip to Question 8. If YES, In the past 12 months, have you had dreams in which you were a man?",
                "08. In the past 12 months, have you felt unhappy about being a woman?",
                "09. In the past 12 months, have you felt uncertain about yourself, at times feeling more like a man and at times feeling more like a woman?",
                "10. In the past 12 months, have you felt more like a man than like a woman?",
                "11. In the past 12 months, have you felt that you did not have anything in common with either men or women?",
                "12. In the past 12 months, have you been bothered by seeing yourself identified as female or having to check the box “F” for female on official forms (e.g., employment applications, driver's license, passport)?",
                "13. In the past 12 months, have you felt comfortable when using women's restrooms in public places?",
                "14. In the past 12 months, have strangers treated you as a man?",
                "15. In the past 12 months, at home, have people you know, such as friends or relatives, treated you as a man?",
                "16. In the past 12 months, have you had the wish or desire to be a man?",
                "17. In the past 12 months, at home, have you dressed and acted as a man?",
                "18. In the past 12 months, at parties or at other social gatherings, have you presented yourself as a man?",
                "19. In the past 12 months, at work or at school, have you presented yourself as a man?",
                "20. In the past 12 months, have you disliked your body because it is female (e.g., having breasts or having a vagina)?",
                "21. In the past 12 months, have you wished to have hormone treatment to change your body into a man's?",
                "22. In the past 12 months, have you wished to have an operation to change your body into a man's (e.g., to have your breasts removed or to have a penis made)?",
                "23. In the past 12 months, have you made an effort to change your legal sex (e.g., on a driver's licence or credit card)?",
                "24. In the past 12 months, have you thought of yourself as a “hermaphrodite” or an “intersex” rather than as a man or woman?",
                "25. In the past 12 months, have you thought of yourself as a “transgendered person”?",
                "26. In the past 12 months, have you thought of yourself as a man?",
                "27. In the past 12 months, have you thought of yourself as a woman?",
            ],
            'choices': ["always", "often", "sometimes", "rarely", "never"],
            'skippable': True,
        })

    return Response({
        # TODO calulate actual scores and result, remove this dummy data
        'score': 7,
        'result type': 'text',
        'result': 'No Gender Dysphoria',
        'refrences': [
            "Deogracias JJ, Johnson LL, Meyer-Bahlburg HF, Kessler SJ, Schober JM, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults. J Sex Res. 2007 Nov;44(4):370-9. doi: 10.1080/00224490701586730. PMID: 18321016.",
            "Singh D, Deogracias JJ, Johnson LL, Bradley SJ, Kibblewhite SJ, Owen-Anderson A, Peterson-Badali M, Meyer-Bahlburg HF, Zucker KJ. The gender identity/gender dysphoria questionnaire for adolescents and adults: further validity evidence. J Sex Res. 2010 Jan;47(1):49-58. doi: 10.1080/00224490902898728. PMID: 19396705.",
        ],
    })
