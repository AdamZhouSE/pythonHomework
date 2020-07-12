"""
下载代码
解压格式为 /Code/CodeRecords/case_id/user_id/xxx.py
"""

import json
import urllib.request
import urllib.parse
import os
import zipfile as z
import requests


def callbackfunc(blocknum, blocksize, totalsize):
    percent = 100 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print("%.2f%%" % percent)


def delete(haveSorted, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        res = f.read()
        data = json.loads(res)
        for code_id in haveSorted:
            if code_id in data.keys():
                del data[code_id]

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def upzip(zip_src, dst_dir):
    fz = z.ZipFile(zip_src, 'r')
    zip_src = fz.namelist()[0]
    fz.extract(zip_src, dst_dir)
    fz = z.ZipFile(zip_src, 'r')
    fz.extract('main.py', dst_dir)


def DL(data: dict, path):
    case_count = 0
    haveSorted = []

    for case_id, details in data.items():
        if case_id not in haveSorted:
            records = details["records"]
            user_count = 0
            for record in records:
                user_id = record["user_id"]
                for up in record["upload_records"]:
                    upload_id = str(up["upload_id"])
                    code_url = up["code_url"]
                    print("下载链接: ", code_url)
                    try:
                        download(case_id, user_id, upload_id, code_url, path)
                    except:
                        continue
                user_count += 1
                print(user_id + "------" + str(user_count))
            case_count += 1
            print(case_id + "-------------------------" + str(case_count))
            haveSorted.append(case_id)
            print(sorted(haveSorted))


def download(case_id, user_id, upload_id, url, path):
    filename = urllib.parse.unquote(os.path.basename(url))

    os.chdir(path)
    # 创建文件夹
    if case_id not in os.listdir(path):
        os.mkdir(case_id)
    os.chdir(path + "/" + case_id)
    path = os.getcwd()

    if user_id not in os.listdir(path):
        os.mkdir(user_id)
    os.chdir(path + "/" + user_id)
    path = os.getcwd()

    # 下载
    if (upload_id + ".py") not in os.listdir(path):
        # urllib.request.urlretrieve(url, filename, callbackfunc)
        r = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(r.content)
        upzip(filename, os.getcwd())
        os.rename("main.py", upload_id + ".py")
        for file in os.listdir(path):
            if file.endswith(".zip"):
                os.remove(file)


if __name__ == '__main__':
    filename = '../Data/Database of Mooctest.json'
    haveSorted = []
    #delete(haveSorted, filename)

    with open(filename, 'r', encoding='utf-8') as f:
        res = f.read()
        data = json.loads(res)
        print(len(data.keys()))
        os.chdir(os.getcwd() + "/CodeRecords")
        DL(data, os.getcwd())
