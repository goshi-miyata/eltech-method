# returnは1箇所にする

## 概要
メソッドの途中でreturnしない

## ルール
returnはメソッド末尾に1つだけ配置する

## 理由
- 処理の流れが分断される
- 見落としの原因になる
- ストーリー性が失われる

## 判断基準
- ifの中でreturnしていないか
- 処理が途中で終わっていないか

## 例

### ✅ OK
int ret;
if (A) {
    ret = calc(1);
} else {
    ret = calc(2);
}
return ret;

### ❌ NG
if (A) {
    return calc(1);
}
return calc(2);
``