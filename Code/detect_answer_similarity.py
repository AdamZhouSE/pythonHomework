import difflib


def get_similarity_ratio(s, t):
    return difflib.SequenceMatcher(None, s, t).quick_ratio()


def extract_file(answerpath):
    with open(answerpath, encoding='utf-8') as answerf:
        # 预处理，将空行和注释行去除
        text = ''
        content_list = answerf.readlines()
        for content in content_list:
            content = content.lstrip()
            if content:
                if not content.startswith("#"):
                    text += content
        # print(text)
        return text


def detect_is_answer(answerpath, codepath):
    similarity_ratio = get_similarity_ratio(extract_file(answerpath), extract_file(codepath))
    # print(similarity_ratio)
    if similarity_ratio >= 0.9:
        return True
    else:
        return False


if __name__ == "__main__":
    answer = 'Test//answer2061.py'
    code = 'Test//245757.py'
    print(detect_is_answer(answer, code))
