from hnh.utils import get_max_score,get_max_score2,get_max_score3

def test_max_p_label():
    hotdog_prop=0.6
    p=[
        {"label": "hot dog", "score": hotdog_prop},
        {"label": "not hot dog", "score": 1-hotdog_prop}
    ]

    assert get_max_score(p)=="hot dog"

##############################################################
def test_max_p_label2():
    hotdog_prop=0.6
    p=[
        {"label": "hot dog", "score": hotdog_prop},
        {"label": "not hot dog", "score": 1-hotdog_prop}
    ]

    assert get_max_score2(p)=="hot dog"

def test_max_p_label3():
    hotdog_prop=0.6
    p=[
        {"label": "hot dog", "score": hotdog_prop},
        {"label": "not hot dog", "score": 1-hotdog_prop}
    ]

    assert get_max_score3(p)=="hot dog"
