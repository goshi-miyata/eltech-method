# 入力値検証

---

## 1. ルール（要約）

- 外部入力を信用してはいけない
- 入力値は必ず検証する
- 想定外の値を受け入れてはいけない
- 入力チェックは利用前に実施する
- メソッド引数も入力値として扱う
- 美しいコードとは安全で可読性の高いコードである

---

## 2. 解説

### セキュアコーディングのお作法（その１：入力値を信用しない）

システム開発において最も危険な思い込みがあります。

それは、

    入力される値は正しい

という思い込みです。

しかし実際には、

- ユーザが誤入力する
- 他システムが不正なデータを送る
- 攻撃者が意図的に異常値を送る

といったことが日常的に発生します。

そのため、外部から受け取る値はすべて疑う必要があります。

---

### 悪い例

```java
int age = Integer.parseInt(request.getParameter("age"));

if(age >= 20)
{
    ...
}
```

このコードは入力値を無条件に利用しています。

もし、

- abc
- -999
- 999999999999

などの値が送信された場合はどうなるでしょうか。

例外発生や異常動作の原因になります。

---

### 正しい例

```java
String ageText = request.getParameter("age");

if(ageText == null)
{
    throw new IllegalArgumentException();
}

int age = Integer.parseInt(ageText);

if(age < 0 || age > 150)
{
    throw new IllegalArgumentException();
}
```

まず入力値を検査し、その後に利用します。

処理よりも先に検証を行うことが重要です。

---

### メソッド引数も信用しない

入力値というと、

- 画面入力
- APIリクエスト

を想像しがちです。

しかし、

```java
public void updateUser(User user)
```

のようなメソッド引数も入力値です。

呼び出し元が誤っている可能性は常に存在します。

---

### 悪い例

```java
public void updateUser(User user)
{
    repository.save(user);
}
```

---

### 正しい例

```java
public void updateUser(User user)
{
    if(user == null)
    {
        throw new IllegalArgumentException();
    }

    repository.save(user);
}
```

---

### なぜ検証するのか

入力値検証の目的は、異常を早期に発見することです。

問題が発生してから調査するのではなく、異常なデータを入口で拒否します。

これはセキュリティ対策であると同時に、品質向上にもつながります。

---

### まとめ

入力値は信用しない。

これはセキュアコーディングの基本原則です。

画面入力だけではなく、

- API入力
- ファイル入力
- DB取得値
- メソッド引数

も含めて検証するようにしてください。

美しいコードとは、安全で可読性の高いコードであると考えます。
