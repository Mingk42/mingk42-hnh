
def get_max_score(p):
    print()
    print(f"당신이 넣은 이미지는")
    print(f"{p[0]['score']*100:.2f}%의 확률로 {p[0]['label']}이며")
    print(f"{p[1]['score']*100:.2f}%의 확률로 {p[1]['label']}입니다.")

    return p[0]['label'] if p[0]['score']>p[1]['score'] else p[1]['label']




##############################################################
def get_score(item):
  return item['score']


def get_max_score2(p):
  max_p = max(p, key=get_score)
  return max_p["label"]


def get_max_score3(p):
  max_p = max(p, key=lambda x: x['score'])
  return max_p["label"]