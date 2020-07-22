"""
下载答案
解压格式为 /Code/Cases/answer.py
"""

import json
import urllib.request
import urllib.parse
import os
import zipfile as z
import requests


def upzip(zip_src, dst_dir):
    fz = z.ZipFile(zip_src, 'r')
    for filename in ["readme.md", ".mooctest/answer.py", ".mooctest/testCases.json"]:
        fz.extract(filename, dst_dir)


def DL(data: dict, path):
    case_count = 0
    haveSorted = []

    for case_id, details in data.items():
        if case_id not in haveSorted:
            case_url = details["case_zip"]
            try:
                download(case_id, case_url, path)
            except:
                continue

            case_count += 1
            print(case_id + "-------------------------" + str(case_count))
            haveSorted.append(case_id)
            # print(sorted(haveSorted))


def download(case_id, url, path):
    filename = urllib.parse.unquote(os.path.basename(url))

    os.chdir(path)
    # 创建文件夹
    if case_id not in os.listdir(path):
        os.mkdir(case_id)
    os.chdir(path + "/" + case_id)
    path = os.getcwd()

    # 下载
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

    #  解压
    upzip(filename, os.getcwd())
    # os.rename("main.py", upload_id + ".py")
    for file in os.listdir(path):
        if file.endswith(".zip"):
            os.remove(file)


if __name__ == '__main__':
    filename = '../Data/updatedDatabase of Mooctest.json'
    haveSorted = []
    # delete(haveSorted, filename)

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        # print(len(data.keys()))
        os.mkdir("Cases")
        os.chdir(os.getcwd() + "/Cases")
        DL(data, os.getcwd())
