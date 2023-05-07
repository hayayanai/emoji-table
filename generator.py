import argparse
import requests


def generate(tone: int = 0) -> dict[str, str]:
    URL = "https://raw.githubusercontent.com/joypixels/emoji-toolkit/master/emoji.json"

    req = requests.get(URL)

    if req.status_code != 200:
        raise Exception(f"Error: HTTP Status Code {req.status_code}")

    emoji_dic = req.json()
    res = {}

    for v in emoji_dic.values():
        if v["category"] == "modifier":
            continue
        names = [v["shortname"]] + v["shortname_alternates"]
        shortest_name = min(names, key=len)

        if shortest_name.count("tone") >= 2:
            continue
        elif shortest_name.count("tone") == 1:
            if "_tone" + str(tone) in shortest_name:
                shortest_name = shortest_name.replace("_tone" + str(tone), "")
            else:
                continue

        emoji = ""
        code_points = v["code_points"]["fully_qualified"]
        if "-" in code_points:
            u_code = "".join([chr(int(c, 16)) for c in code_points.split("-")])
            emoji = u_code.encode("utf-16", "surrogatepass").decode("utf-16")
        else:
            emoji = chr(int(code_points, 16))

        res[shortest_name] = emoji
    return res


def output(dic: dict) -> None:
    for code, v in dic.items():
        print(code, v, sep="\t")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate romantable')
    parser.add_argument("-t", "--tone", choices=range(0, 6),
                        default=0, type=int, help="skin tone")
    args = parser.parse_args()
    output(generate(args.tone))
