# The Hermit 日本語化 (Slay the Spire 2)

Slay the Spire 2 の追加キャラクターMOD **The Hermit** の日本語化MODです。
カード・レリック・パワー・キーワード・建築家との会話を日本語で表示します。

## 必要なもの
- [The Hermit](https://steamcommunity.com/app/2868840/workshop/)(Steamワークショップ)
- BaseLib(The Hermit の前提MOD)

## 導入方法
1. [Releases](../../releases) から `HermitMod_JPN.zip` をダウンロードします。
2. 展開してできた `HermitMod_JPN` フォルダを、ゲームの `mods` フォルダに入れます。
   - 例: `C:\Program Files (x86)\Steam\steamapps\common\Slay the Spire 2\mods\HermitMod_JPN`
3. ゲームを起動し、「Mod設定」で **HermitMod_JPN** を有効にして再起動します。
4. 言語設定を日本語にします。

## 仕組み
BaseLib/ゲーム本体は `res://<MODのID>/localization/<言語>/` を読み込みます。
この日本語化MODは `res://HermitMod/localization/jpn/` にファイルを追加するだけの、PCKのみのMODです。本体のMODは改変しません。

## ビルド
```
python src/build_loc.py     # pack/ に日本語JSONを生成
python src/build_pck.py     # dist/HermitMod_JPN/ にPCKとmanifestを生成
```

## 用語
デッドオン(Dead On) / 打撲(Bruise) / 集中(Concentrate) / 頑強(Rugged) / プレート(Plating) など。
ゲーム本体の公式日本語に合わせています。誤訳・改善提案はIssueへどうぞ。

## クレジット
元MOD: The Hermit(Hermit Mod Team, KenCagg90, TheBoggart)。翻訳のみを提供する非公式の有志MODです。

## ライセンス
MIT(翻訳部分)。元MODの文章の権利は元作者にあります。
