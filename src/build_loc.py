# -*- coding: utf-8 -*-
"""Hermit MOD 日本語ローカライズ生成(キーは英語版eng/*.jsonと同一)"""
import json, os
P = "HERMITMOD-"
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pack", "HermitMod", "localization", "jpn")
os.makedirs(out, exist_ok=True)


def save(name, d):
    with open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


DO = "[gold]デッドオン[/gold]"
# ---- cards: id -> (title, description[, extras])
C = {
"STRIKE_HERMIT": ("ストライク", "{Damage:diff()}ダメージを与える。"),
"DEFEND_HERMIT": ("防御", "{Block:diff()}[gold]ブロック[/gold]を得る。"),
"SNAPSHOT": ("スナップショット", "{Damage:diff()}ダメージを与える。\n" + DO + ": 防がれなかったダメージと同じだけ[gold]ブロック[/gold]を得る。"),
"DESPERADO": ("デスペラード", "{Damage:diff()}ダメージを与える。\nこの戦闘中、このカードのダメージを2倍にする。コストが1増える。"),
"HEADSHOT": ("ヘッドショット", "{Damage:diff()}ダメージを与える。\n" + DO + ": ダメージを2倍にする。"),
"QUICKDRAW": ("クイックドロウ", "{Damage:diff()}ダメージを与える。\nカードを{Cards:diff()}枚引く。\n次のターン、引く枚数が1枚減る。"),
"WIDE_OPEN": ("がら空き", "{Damage:diff()}ダメージを与える。\n[gold]弱体[/gold]{VulnerablePower:diff()}を付与する。"),
"COVET": ("渇望", "カードを1枚捨てる。\nカードを{Cards:diff()}枚引く。\n捨てた[gold]呪い[/gold]は廃棄される。"),
"HIGH_CALIBER": ("大口径", "{Damage:diff()}ダメージを与える。\n[gold]ストライク{IfUpgraded:show:+3|+2}[/gold]を1枚手札に加える。"),
"BODY_ARMOR": ("ボディアーマー", "カードを1枚捨てる。\n{Block:diff()}[gold]ブロック[/gold]を得る。\nそれがアタック以外なら、もう一度{Block:diff()}[gold]ブロック[/gold]を得る。"),
"SNIPE": ("狙撃", "{IfUpgraded:show:[gold]集中[/gold]する。\n|}このターン次に発動する" + DO + "の効果が2回発動する。"),
"CALLED_SHOT": ("狙い撃ち", "{Damage:diff()}ダメージを与える。\nこのターン最後にプレイしたカードが" + DO + "を発動していた場合、カードを1枚引く。"),
"DISSOLVE": ("溶解", "{Block:diff()}[gold]ブロック[/gold]を得る。\n次の2ターンの開始時に[gold]ブロック[/gold]を失わない。"),
"BLACK_WIND": ("黒き風", "失ったHPと同じだけダメージを与える。"),
"PURGATORY": ("煉獄", "すべての敵に{Damage:diff()}ダメージを与える。"),
"SHADOW_CLOAK": ("影の外套", "呪いカードを引くか[gold]廃棄[/gold]するたび、{ShadowCloakPower:diff()}[gold]ブロック[/gold]を得る。"),
"FATAL_DESIRE": ("致命の欲望", "ターン開始時、カードを2枚引き、[gold]怪我[/gold]を1枚手札に加える。"),
"GAMBIT": ("ギャンビット", "[gold]捨て札[/gold]からランダムなアタックを{Cards:diff()}枚手札に加える。このターン、それらのコストが1減る。"),
"ROUGHHOUSE": ("大乱闘", "{Damage:diff()}ダメージを与える。" + DO + ":\n{Block:diff()}[gold]ブロック[/gold]を得る。"),
"MALICE": ("悪意", "カードを1枚[gold]廃棄[/gold]する。\n{Damage:diff()}ダメージを与える。\n呪いを廃棄した場合、代わりにすべての敵に{Damage:diff()}ダメージを与える。", {"selectionScreenPrompt": "[gold]廃棄[/gold]するカードを選択"}),
"DEADEYE": ("デッドアイ", "{Damage:diff()}ダメージを与える。\n" + DO + ":\n[gold]筋力[/gold]{StrengthPower:diff()}を得る。"),
"GHOSTLY_PRESENCE": ("幽かな気配", "{Block:diff()}[gold]ブロック[/gold]を得る。\n" + DO + ": すべての敵に[gold]脱力[/gold]{WeakPower:diff()}を付与する。"),
"ADAPT": ("適応", "ターン開始時、カードを1枚[gold]廃棄[/gold]して8[gold]ブロック[/gold]を得ることができる。"),
"DIVE": ("ダイブ", "{Block:diff()}[gold]ブロック[/gold]を得る。\n" + DO + ":\n[gold]プレート[/gold]{IfUpgraded:show:2|1}を得る。"),
"FLASH_POWDER": ("閃光粉", "{Block:diff()}[gold]ブロック[/gold]を得る。\nすべての敵の[gold]筋力[/gold]を{IfUpgraded:show:2|1}下げる。"),
"ROULETTE": ("ルーレット", "{Damage:diff()}ダメージを与える。\n手札をすべて捨てる。\n同じ枚数のカードを引く。"),
"MIDNIGHT": ("真夜中", "{Block:diff()}[gold]ブロック[/gold]を得る。\n[gold]迫りくる破滅[/gold]を1枚手札に加える。"),
"GLARE": ("睨みつけ", "[gold]脱力[/gold]{WeakPower:diff()}と[gold]弱体[/gold]を付与する。"),
"TAKE_COVER": ("遮蔽物へ", "コスト0の[gold]防御[/gold]を1枚手札に加え、それをX{IfUpgraded:show:+1|}回アップグレードする。"),
"MISFIRE": ("不発", "{Damage:diff()}ダメージを与える。\n[gold]不器用[/gold]を1枚[gold]山札[/gold]に混ぜる。"),
"SPRAY_PRAY": ("乱射", "ランダムな敵に{Damage:diff()}ダメージを3回与える。\n[gold]疑念[/gold]を1枚[gold]山札[/gold]に混ぜる。"),
"HERMIT_SCAVENGE": ("漁る", "[gold]プレート[/gold]{PlatingPower:diff()}を得る。\n" + DO + ": {IfUpgraded:show:10|5}[gold]ゴールド[/gold]を得る。"),
"IMPENDING_DOOM": ("迫りくる破滅", "ターン終了時にこれが" + DO + "の位置にある場合、{Multiplayer:自分とすべての敵|全員}に13ダメージを与える。"),
"MEMENTO_CARD": ("形見", "{Multiplayer:自分とすべての敵|全員}に[gold]弱体[/gold]{VulnerablePower:diff()}を付与する。"),
"SHORT_FUSE": ("短い導火線", "{Damage:diff()}ダメージを与える。\nこのターンにプレイした[gold]ストライク[/gold]か[gold]防御[/gold]1枚につき、コストが1減る。"),
"GRUDGE": ("怨恨", "すべての敵に{CalculatedDamage:diff()}ダメージを与える。\n所持している呪いカード1枚につき{ExtraDamage:diff()}ダメージ追加。"),
"HERMIT_SPITE": ("意趣返し", "手札のプレイ不可カードをすべて[gold]廃棄[/gold]する。\n{Block:diff()}[gold]ブロック[/gold]を得る。\nカードを{Cards:diff()}枚引く。"),
"MANIFEST": ("顕現", "{Block:diff()}[gold]ブロック[/gold]を得る。\n[gold]腐敗[/gold]を1枚手札に加える。"),
"FEINT": ("フェイント", "{Block:diff()}[gold]ブロック[/gold]を得る。\nすべての敵に[gold]打撲[/gold]{BruisePower:diff()}を付与する。"),
"LOW_PROFILE": ("低姿勢", "{Block:diff()}[gold]ブロック[/gold]を得る。\n自分にかかっているデバフ1つにつき、さらに{IfUpgraded:show:5|4}[gold]ブロック[/gold]を得る。"),
"HORROR": ("恐怖", "すべての敵に[gold]打撲[/gold]{BruisePower:diff()}を付与する。\nこのターン、[gold]打撲[/gold]が解除されない。"),
"NO_HOLDS_BARRED": ("なりふり構わず", "すべての敵に{Damage:diff()}ダメージを与え、[gold]打撲[/gold]{BruisePower:diff()}を付与する。\n次のターン、得るエナジーが1減る。"),
"CHEAT": ("イカサマ", "[gold]山札[/gold]の上から{Cards:diff()}枚のうち1枚をプレイする。\n" + DO + ": その" + DO + "の効果も発動する。", {"selectionScreenPrompt": "プレイするカードを選択"}),
"VANTAGE": ("好位置", "{Block:diff()}[gold]ブロック[/gold]を得る。\n" + DO + ": カードを引き、{IfUpgraded:show:2枚|1枚}アップグレードする。"),
"BRAWL": ("乱闘", "ターン開始時、すべての敵に[gold]打撲[/gold]{BruisePower:diff()}を付与する。"),
"COMBO": ("コンボ", "各ターン最初に発動した{IfUpgraded:show:2枚の|}" + DO + "カードを手札に戻す。"),
"BIG_SHOT": ("煙る銃口", DO + "の効果を発動するたび、次のアタックのダメージが{BigShotPower:diff()}増加する。"),
"OVERWHELMING_POWER": ("圧倒的な力", "{Energy:energyIcons()}を得る。\nカードを{Cards:diff()}枚引く。\nエナジー0でターンを終えるたび、HPを{HpLoss:diff()}失う。"),
"MAINTENANCE": ("手入れ", "この戦闘中、ストライクのダメージが{MaintenanceStrikePower:diff()}増加する。\n[gold]敏捷[/gold]{DexterityPower:diff()}を得る。\nプレイするたび、このカードのコストが1増える。"),
"ETERNAL_FORM": ("永遠の姿", "各ターン開始時に引いたプレイ可能なカードのうち最初の4枚は、そのターンのコストが1減る。"),
"FULLY_LOADED": ("フル装填", "[gold]山札[/gold]にあるすべての[gold]ストライク[/gold]と[gold]防御[/gold]を手札に加える。"),
"GESTALT": ("ゲシュタルト", "[gold]弱体[/gold]{VulnerablePower:diff()}を得る。\n[gold]頑強[/gold]{RuggedPower:diff()}を得る。"),
"ROUNDHOUSE_KICK": ("回し蹴り", "すべての敵に{Damage:diff()}ダメージを与える。\nアタックの意図がない敵を[gold]スタン[/gold]させる。"),
"CURSED_WEAPON": ("呪われた武器", "HPを{HpLoss:diff()}失う。\n{Damage:diff()}ダメージを与える。\nすべての[gold]呪われた武器[/gold]のダメージを永続的に1増やす。"),
"ENERVATE": ("衰弱", "{Damage:diff()}ダメージを与える。\n" + DO + ":\nエナジーを得て、カードを1枚引く。"),
"HERMIT_RICOCHET": ("跳弾", "{Damage:diff()}ダメージを与える。このターン発動した" + DO + "の効果1つにつき、ランダムな敵に対して繰り返す。"),
"TRACKING_SHOT": ("追尾射撃", "[gold]集中[/gold]する。\n{Damage:diff()}ダメージを2回与える。"),
"LONE_WOLF": ("一匹狼", "カードを1枚選ぶ。\nそのカードのコストはこのターン0になる。\n残りの手札を捨てる。", {"selectionScreenPrompt": "残すカードを選択"}),
"HIGH_NOON": ("正午の決闘", "[gold]ストライク[/gold]か[gold]防御[/gold]をプレイするたび、カードを1枚引く。"),
"REPRIEVE": ("猶予", "HPを{Heal:diff()}回復する。"),
"TAKE_AIM": ("狙いを定める", "{IfUpgraded:show:[gold]集中[/gold]する。\n|}ターン開始時、[gold]集中[/gold]する。"),
"MAGNUM": ("マグナム", "カードを6枚捨てる。\n捨てたカード1枚につき{Damage:diff()}ダメージを与える。"),
"DETERMINATION": ("決意", "自分にデバフが付与されるたび、[gold]筋力[/gold]1を得る。"),
"SHOWDOWN": ("決闘", "{Damage:diff()}ダメージを与える。\n手札の[gold]ストライク[/gold]をすべてプレイする。"),
"LUCK_OF_THE_DRAW": ("引きの強さ", "合計コストが{IfUpgraded:show:4|3}以上になるまでカードを引く。"),
"COALESCENCE": ("結合", "{Block:diff()}[gold]ブロック[/gold]を得る。\nこのターン、最大{CoalescencePower:diff()}枚のカードを[gold]保留[/gold]する。"),
"PISTOL_WHIP": ("ピストルウィップ", "{Damage:diff()}ダメージを与える。\n[gold]打撲[/gold]{BruisePower:diff()}を付与する。"),
"DEAD_MANS_HAND": ("死者の手札", "手札をすべて捨てる。\n[gold]山札[/gold]から最もレアリティの高いカードを{Cards:diff()}枚手札に加える。"),
"DEAD_OR_ALIVE": ("生死問わず", "{Damage:diff()}ダメージをX回与える。\nリーサルなら[gold]賞金[/gold]を得る。"),
"GOLDEN_BULLET": ("黄金の弾丸", "{Damage:diff()}ダメージを与える。\nリーサルなら、このカードのコストを永続的に1減らす。"),
"HOLE_UP": ("立てこもり", "{Block:diff()}[gold]ブロック[/gold]を得る。\n[gold]脱力[/gold]{WeakPower:diff()}を得る。"),
"ITCHY_TRIGGER": ("疼く引き金", "{Damage:diff()}ダメージを与える。\n" + DO + ": このターン、手札のランダムなカード1枚のコストを{IfUpgraded:show:2|1}減らす。"),
"EYE_OF_THE_STORM": ("嵐の目", "[gold]集中[/gold]する。\nエナジーを最大まで回復する。"),
"FINAL_CANTER": ("最後の駆け足", "手札の呪い1枚につき{ExtraDamage:diff()}ダメージを与える。\n{InCombat:(現在は合計{CalculatedDamage:diff()}ダメージ)|}"),
"HEROIC_BRAVADO": ("勇者の虚勢", "[gold]頑強[/gold]1を得る。\nこの戦闘中、このカードのコストが{IfUpgraded:show:1|2}増える。"),
"FROM_BEYOND": ("彼方より", "[gold]廃棄札[/gold]のカード1枚につき、ランダムな敵がHPを{HpLoss:diff()}失う。"),
"VIRTUE": ("美徳", "自分にかかっているすべてのデバフを{IfUpgraded:show:2|1}減らす。"),
"FLEETING_TIME": ("束の間の時", "ターン開始時、ランダムな[gold]呪い[/gold]を1枚捨て札に加える。\n所持している呪い1枚につき、カードのダメージとブロックが増加する。"),
"AVARICE": ("貪欲", "好きな枚数のカードを捨てる。同じ枚数のカードを引く{IfUpgraded:show:(引いたカードはアップグレードされる)|}。\n捨てた状態異常や呪いは[gold]廃棄[/gold]される。", {"selectionScreenPrompt": "捨てるカードを選択"}),
"SHADOWMEND": ("影の癒し", "すべてのプレイヤーは手札の呪いと状態異常を[gold]廃棄[/gold]する。"),
"ABYSSAL_BEACON": ("深淵の灯火", "{Energy:energyIcons()}を得る。\n味方が[gold]脱力[/gold]、[gold]弱体[/gold]、[gold]脆弱[/gold]を受ける場合、代わりに自分が受ける。"),
"BIG_BRUISER": ("大暴れ", "自分が敵に付与した[gold]打撲[/gold]の恩恵をすべてのプレイヤーが受ける。\nすべての敵に[gold]打撲[/gold]{BruisePower:diff()}を付与する。"),
}
cards = {}
for k, v in C.items():
    cards[P + k + ".title"] = v[0]
    cards[P + k + ".description"] = v[1]
    if len(v) > 2:
        for ek, ev in v[2].items():
            cards[P + k + "." + ek] = ev
save("cards.json", cards)

# ---- keywords
save("card_keywords.json", {
    P + "DEAD_ON.title": "デッドオン",
    P + "DEAD_ON.description": "デッドオンのカードは、手札の中央にあるとボーナス効果を発揮する。",
    P + "DEADON.title": "デッドオン",
    P + "DEADON.description": "デッドオンのカードは、手札の中央にあるとボーナス効果を発揮する。",
    P + "CONCENTRATE.title": "集中",
    P + "CONCENTRATE.description": "集中している間にプレイした次のデッドオンカードは、位置に関係なく効果を発動する。ターン終了時に解除される。",
    P + "BRUISE.title": "打撲",
    P + "BRUISE.description": "打撲状態の対象は、ハーミットから追加のアタックダメージを受ける。ターン終了時に解除される。",
    P + "RUGGED.title": "頑強",
    P + "RUGGED.description": "次に受けるアタックダメージを2に軽減する。",
    P + "BOUNTY.title": "賞金",
    P + "BOUNTY.description": "通常の敵: 15ゴールド。エリート: 40ゴールド。ボス: 100ゴールド。",
    P + "STUN.title": "スタン",
    P + "STUN.description": "スタンした敵は自分のターンを飛ばす。",
})

# ---- characters
save("characters.json", {
    P + "HERMIT.title": "ハーミット",
    P + "HERMIT.titleObject": "ハーミット",
    P + "HERMIT.description": "無法の時代から来た、過去に苛まれる疲れた射手。\n手札のカードの位置を操り、致命的な[gold]デッドオン[/gold]効果を発動させる。",
    P + "HERMIT.pronounSubject": "彼",
    P + "HERMIT.pronounObject": "彼",
    P + "HERMIT.possessiveAdjective": "彼の",
    P + "HERMIT.pronounPossessive": "彼の",
    P + "HERMIT.goldMonologue": "[sine]この金があれば……弾薬くらいは買えるか……[/sine]",
    P + "HERMIT.eventDeathPrevention": "まだだ……やり残したことがある……",
    P + "HERMIT.aromaPrinciple": "[sine][blue]……火薬の匂い……[/blue][/sine]",
    P + "HERMIT.cardsModifierTitle": "ハーミットのカード",
    P + "HERMIT.cardsModifierDescription": "報酬やショップにハーミットのカードが出現するようになる。",
    P + "HERMIT.banter.alive.endTurnPing": "……",
    P + "HERMIT.banter.dead.endTurnPing": "……",
    P + "HERMIT.unlockText": "[pink]{Prerequisite}[/pink]で1回プレイして、このキャラクターをアンロック。",
})

# ---- powers: id -> (title, description[, smartDescription[, extras]])
W = {
"CONCENTRATION_POWER": ("集中", "このターン次にプレイする" + DO + "カードは、位置に関係なく効果を発動する。"),
"HIGH_NOON_POWER": ("正午の決闘", "[gold]ストライク[/gold]か[gold]防御[/gold]をプレイするたび、カードを{Amount}枚引く。"),
"FATAL_DESIRE_POWER": ("致命の欲望", "ターン開始時、カードを2枚引き、[gold]怪我[/gold]を1枚手札に加える。"),
"SHADOW_CLOAK_POWER": ("影の外套", "呪いを引くか[gold]廃棄[/gold]するたび、{Amount}[gold]ブロック[/gold]を得る。"),
"TAKE_AIM_POWER": ("狙いを定める", "ターン開始時、[gold]集中[/gold]する。"),
"ADAPT_POWER": ("適応", "ターン開始時、最大{Amount}枚のカードを[gold]廃棄[/gold]して、それぞれ8[gold]ブロック[/gold]を得る。"),
"BRUISE_POWER": ("打撲", "このターン、対象はハーミットから追加で{Amount}のアタックダメージを受ける。"),
"HORROR_POWER": ("恐怖", "{Amount}ターンの間、打撲が解除されない。"),
"COMBO_POWER": ("コンボ", "このターン最初に発動した{Amount}枚の" + DO + "カードを手札に戻す。"),
"BIG_SHOT_POWER": ("煙る銃口", DO + "の効果を発動するたび、次のアタックのダメージが{Amount}増加する。"),
"BRAWL_POWER": ("乱闘", "ターン開始時、すべての敵に打撲{Amount}を付与する。"),
"RUGGED_POWER": ("頑強", "次に{Amount}回、防がれなかったアタックダメージを受ける時、それを2に軽減する。"),
"ETERNAL_POWER": ("永遠の力", "各ターン開始時に引いたプレイ可能なカードのうち最初の4枚は、そのターンのコストが{Amount}減る。"),
"OVERWHELMING_POWER_POWER": ("圧倒的な力", "エナジー0でターンを終えるとHPを{Amount}失う。"),
"MAINTENANCE_STRIKE_POWER": ("手入れ", "[gold]ストライク[/gold]のダメージが{Amount}増加する。"),
"DETERMINATION_POWER": ("決意", "デバフが付与されるたび、[gold]筋力[/gold]{Amount}を得る。"),
"DRAINED_POWER": ("消耗", "次のターン、得るエナジーが{Amount}減る。"),
"BOUNTY_POWER": ("賞金", "敵が死亡した時、戦闘の種類に応じたゴールドを得て、賞金が1減る。(残り{Amount}回)", "キルで得たゴールドを記録する。"),
"DISSOLVE_BARRICADE_POWER": ("溶解", "次の{Amount}ターンの開始時に[gold]ブロック[/gold]を失わない。"),
"SNIPE_POWER": ("狙撃", "このターン次に発動する{Amount}回の" + DO + "の効果が2回発動する。"),
"COALESCENCE_POWER": ("結合", "ターン終了時、最大{Amount}枚のカードを[gold]保留[/gold]する。", None, {"selectionScreenPrompt": "保留するカードを選択"}),
"REPRIEVE_POWER": ("猶予", "このターンの後、{Amount}回の追加ターンを得る。"),
"RYE_STALK_POWER": ("ライ麦の茎", "このターン終了時、好きな枚数のカードを[gold]保留[/gold]する。"),
"DRAW_REDUCTION_POWER": ("ドロー減少", "次のターン、引く枚数が{Amount}枚減る。"),
"FLEETING_TIME_POWER": ("束の間の時", "ターン開始時、ランダムな呪いを1枚捨て札に加える。所持している呪い1枚につき、カードのダメージが{Amount}、ブロックが{Amount}増加する。"),
"ABYSSAL_BEACON_POWER": ("深淵の灯火", "味方が[gold]脱力[/gold]、[gold]弱体[/gold]、[gold]脆弱[/gold]を受ける場合、代わりに自分が受ける。", "味方の脱力・弱体・脆弱を自分に引き受ける。"),
"BIG_BRUISER_POWER": ("大暴れ", "自分が敵に付与した[gold]打撲[/gold]の恩恵をすべてのプレイヤーが受ける。"),
}
powers = {}
for k, v in W.items():
    powers[P + k + ".title"] = v[0]
    powers[P + k + ".description"] = v[1]
    powers[P + k + ".smartDescription"] = v[2] if len(v) > 2 and v[2] else v[1]
    if len(v) > 3:
        for ek, ev in v[3].items():
            powers[P + k + "." + ek] = ev
save("powers.json", powers)

# ---- relics
R = {
"OLD_LOCKET": ("古いロケット", "色褪せた写真が入っている。", "各戦闘開始時、[gold]形見[/gold]を1枚手札に加える。"),
"RYE_STALK": ("ライ麦の茎", "ずっと噛んでいたのに、まだ新品同様だ。", "敵のターン中にHPを失うたび、カードを1枚引く。"),
"SHOTGLASS": ("ショットグラス", "注いだ液体は何か別のものに変わる。", "各戦闘で最初の2回ポーションを使用した時、ランダムなポーションを得る。各戦闘でポーションは2回までしか使用できない。"),
"HORSESHOE": ("蹄鉄", "幸運のお守り。誰かが失くして困っているだろう。", "[gold]脱力[/gold]、[gold]脆弱[/gold]、[gold]弱体[/gold]を受ける時、付与される数値が1少なくなる。"),
"SPYGLASS": ("望遠鏡", "ケスティン・ハイフィンの持ち物。", "[gold]集中[/gold]状態でターンを終えた場合、次のターンにエナジーを追加で1得る。"),
"RED_SCARF": ("赤いスカーフ", "暖かくてふわふわだ。", "敵に新しいデバフを付与するたび、3[gold]ブロック[/gold]を得る。"),
"DENTED_PLATE": ("へこんだ装甲板", "いくつもの弾丸がまだ食い込んでいる。", "HPが50%以下の間、ターン開始時にエナジーを得て、カードを1枚引く。"),
"PET_GHOST": ("ペットのゴースト", "かわいそうに。", "各戦闘で1回だけ、HPが0になるはずのダメージを無効にする。"),
"CHARRED_GLOVE": ("焦げた手袋", "手袋の一部は、この世のものではない燃えさしで今も光っている。", "[gold]呪い[/gold]を引くたび、次のアタックのダメージが3増加する。"),
"CLASPED_LOCKET": ("留め金のロケット", "もう開かない。", "[gold]古いロケット[/gold]と入れ替わる。各ターン最初に呪いを引いた時、それを[gold]廃棄[/gold]し、カードを2枚引く。入手時、[gold]怪我[/gold]を2枚得る。"),
"STRAIGHT_RAZOR": ("西洋剃刀", "より綺麗に剃るために……", "デッキからカードを削除するか[gold]変化[/gold]させるたび、HPを15回復する。"),
"BRASS_TACKS": ("真鍮の鋲", "この鋲の輝きは決して褪せないようだ。", "ターン終了時、2[gold]ブロック[/gold]を得る。"),
"BLACK_POWDER": ("黒色火薬", "取り扱い注意。", DO + "の効果を発動するたび、すべての敵に2ダメージを与える。"),
"BROKEN_TOOTH": ("折れた歯", "人間の顎から抜けたにしては大きすぎるようだ……", "エリートの敵を倒すたび、HPを7回復し、35ゴールドを得る。"),
}
relics = {}
for k, (t, fl, d) in R.items():
    relics[P + k + ".title"] = t
    relics[P + k + ".flavor"] = fl
    relics[P + k + ".description"] = d
save("relics.json", relics)

# ---- ancients (建築家との会話)
A = "THE_ARCHITECT.talk.HERMITMOD-HERMIT."
save("ancients.json", {
    A + "0-0r.char": "[b]大した家を建てたもんだ。[/b]\n上へ行くほど意地が悪くなる。どこかを思い出すぜ。",
    A + "0-0r.next": "続ける",
    A + "0-1r.ancient": "銃使いか。粗野で、奔放で、一世紀も時代遅れだ。スパイアは設計図であり、お前はそこに紛れ込んだ染みに過ぎない。",
    A + "0-1r.next": "返答する",
    A + "0-2r.char": "もっとマシな奴らにもっとひどい呼ばれ方をしてきたさ。\n……それでも、まだ消されちゃいねえがな。",
    A + "0-attack": "両方",
    A + "1-0r.ancient": "戻ったか。同じ埃、同じコート、後ろには同じ死者たち。\n奴らは一度でも、お前に立ち止まれと言ったか?",
    A + "1-0r.next": "装填する",
    A + "1-1r.char": "毎晩な。\n[b]だが、まだ聞いちゃいねえ。[/b]",
    A + "1-1r.next": "続ける",
    A + "1-2r.ancient": "感傷か。鉛より重いくせに、一度たりとも銃弾を止めたことはない。",
    A + "1-attack": "両方",
    A + "2-0r.ancient": "この階層がお前を飲み込み続けて、何度目だ? 教訓が身に染みるまで、あと何度かかる?",
    A + "2-0r.next": "返答する",
    A + "2-1r.char": "あんたが階段を作り続ける限り……\n俺はそれをすり減らし続けるさ。",
    A + "2-1r.next": "続ける",
    A + "2-2r.ancient": "[jitter][red]ならば、掃き捨てられるがいい。[/red][/jitter]",
    A + "2-attack": "両方",
})
print("ok", len(cards), len(powers), len(relics))
