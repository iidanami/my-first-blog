from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def diagnosis(request):
    if request.method == 'GET':
        template = loader.get_template("diagnosis/input.html")
        return HttpResponse(template.render({}, request))
        
    elif request.method == 'POST':
        fortune = ["大吉","中吉","小吉","吉","末吉","凶","大凶","ゴミ"]
        item = [
        "バラの花束","万年筆","香水","シャンデリア",
        "折りたたみ傘","アロハシャツ","ギザ十","マグカップ",
        "ミトン","ビーサン","下駄","蝶ネクタイ",
        "二千円札","まねき猫","黒縁メガネ","タロットカード",
        "特にない","クリップ","アルカリ電池","カップラーメン",
        "鈴","トイレットペーパー","ビニールハウス","オセロ盤",
        "仙豆","牛乳","ポリタンク","お金",
        "ピラミッド","自由の女神が持ってるアレ","アインシュタイン","ショッキングピンクの靴",
        "イチゴパンツ","ガスボンベ","心の地図","コンパス",
        "全身タイツ","カプセルトイ","電動歯ブラシ","うさ耳カチューシャ",
        "アフロ","妖刀","２Lコーラ（キャップを捨てるとなお良い）","ドリアン",
        "オムツ","もみあげ","愛嬌","へその緒",
        "アジアゾウ","腕時計","勇者の剣","マスク",
        "シイタケ","宇宙食","メタリックブルーの上着","ゴミ",
        ]
        now = datetime.today()
        date_num = now.year + now.month + now.day
        name_num = len(request.POST['name'])
        print(request.POST['name'])
        name_num = name_num % date_num
        num = date_num + name_num
        f_num = num % 7
        num = num % 56
    
        your_item = item[num]
        your_fortune = fortune[f_num]
        context = {
            'fortune': your_fortune,
            'lucky_item': your_item,
        }
        return render(request, 'diagnosis/output.html', context)
