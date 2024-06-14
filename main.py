from PIL import Image
import os
import cv2
import numpy as np
import json
import random


def main():
    print("OpenCV Version:", cv2.__version__)
    print("Pillow Version:", Image.__version__)
    print("==========================")
    print("Select the game mode you want to play.")
    print("1 : Abbreviation")
    print("2 : Icon")
    mode = input()
    if mode == "1":
        abbreviation_game()
    elif mode == "2":
        icon_game()
    else:
        print("Invalid input. Please enter 1 or 2.")
        input("Press Enter to continue, and ctrl+C to exit the program.")


def abbreviation_game():
    score = 0
    print("Let's play the abbreviation game!")
    print("Note that every single answer should be in lowercase.")
    input("Press Enter to start the game.")
    with open("./dicts/with_ abbreviation.json", encoding='utf-8') as f_param:
        json_data = json.load(f_param)
        questions = random.sample(json_data["services"], len(json_data["services"]))
    for num, i in enumerate(questions):
        print(" ")
        print("=================")
        print("question No." + str(num+1))
        print(i["abbreviation"])
        guessed = input("What does this abbreviation suggests? : ")
        if guessed == i["service_name"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect...")
        print("The answer is " + i["service_name"])
        print(i["description"])
        input("Press Enter to continue.")

    print("=================")
    input("Press Enter to see the score.")
    print("Your score is " + str(score) + "/" + str(len(json_data["services"])))


def icon_game():
    score = 0
    print("Let's play the icon game!")
    print("Note that every single answer should be in a number in options.")
    input("Press Enter to start the game.")
    with open("./dicts/with_ abbreviation.json", encoding='utf-8') as f_param:
        json_data = json.load(f_param)
        questions_ab = random.sample(json_data["services"], len(json_data["services"]))
    with open("./dicts/no_ abbreviation.json", encoding='utf-8') as f_param:
        json_data = json.load(f_param)
        questions_non = random.sample(json_data["services"], len(json_data["services"]))
    questions = questions_ab + questions_non
    for i in questions:
        if i["icon"] is None:
            questions.remove(i)
    length = len(questions)
    for num, i in enumerate(questions):
        print(" ")
        print("=================")
        print("question No." + str(num+1))
        print(" ")
        img = cv2.imread(i["icon"])
        image_print(img)
        options = rand_ints_nodup(0, length-2, 3)
        ans_idx = rand_ints_nodup(0, 3, 1)[0]
        for j, k in enumerate(options):
            if k >= num:
                options[j] += 1

        print(" ")
        print("Options are.....")
        options = options[:ans_idx] + ["null"] + options[ans_idx:]
        for op_num in range(4):
            if str(op_num) == str(ans_idx):
                print(str(op_num) + " :" + i["service_name"])
            else:
                print(str(op_num) + " :" + questions[options[op_num]]["service_name"])

        guessed = input("Whose service icon is this? : ")
        if guessed == str(ans_idx):
            print("Correct!")
            score += 1
        else:
            print("Incorrect...")
        print("The answer is " + i["service_name"])
        print(i["description"])
        input("Press Enter to continue.")

    print("=================")
    input("Press Enter to see the score.")
    print("Your score is " + str(score) + "/" + str(len(questions)))


def rand_ints_nodup(a, b, k):
    ns = []
    while len(ns) < k:
        n = random.randint(a, b)
        if not n in ns:
            ns.append(n)
    return ns


def image_print(image, wid=30):
    density = list("MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. ")
    LEN = len(density)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (int(wid*2), int(wid)))
    for i in range(resized.shape[0]):
        s = ""
        for j in range(resized.shape[1]):
            s += density[(LEN-1)-resized[i][j]//(256//LEN)]
        print(s)

def image_read(path):

    #画像の読み込み
    im = Image.open(path)

    #表示
    im.show()

    #画像をarrayに変換
    im_list = np.asarray(im)

    #貼り付け
    plt.imshow(im_list)

    #表示
    plt.show()


if __name__ == "__main__":
    main()