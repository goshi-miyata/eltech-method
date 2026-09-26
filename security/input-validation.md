# 入力値検証

---

## 参考ルール

- IDS14-J hiddenが指定された入力欄の内容を信用しない
- SEC02-J 信頼できない入力値に基づいてセキュリティチェックを行わない
- MET00-J メソッドの引数を検証する
- MET01-J メソッド引数の検証にassertを使わない

---

## 1. ルール（要約）

- クライアントから送信される値を信用してはいけない
- hidden項目の値を信用してはいけない
- セキュリティ判定を入力値に依存してはいけない
- メソッド引数は検証する
- 引数検証にassertを使用してはいけない
- 美しいコードとは安全で可読性の高いコードである

---

## 2. 解説

### セキュアコーディングのお作法（その１：入力値を信用しない）

システム開発において最も危険な思い込みがあります。

それは、

    クライアントから送信された値は正しい

という思い込みです。

しかし実際には、

- ブラウザ開発者ツール
- HTTPプロキシ
- 自作プログラム

などを利用して、
送信内容は容易に改ざんできます。

そのため、

- hidden項目
- URLパラメータ
- フォーム入力
- Cookie

などは全て信用してはいけません。

---

### 悪い例

```java
String role = request.getParameter("role");

if ("ADMIN".equals(role))
{
    deleteUser(id);
}
```

一見問題ないように見えます。

しかし攻撃者が以下のように送信した場合はどうでしょう。

```text
role=ADMIN
```

本来管理者ではない利用者が
管理者機能を実行できる可能性があります。

---

### 正しい例

```java
User user = session.getUser();

if (user.isAdmin())
{
    deleteUser(id);
}
```

権限判定はサーバ側で保持している
認証情報を利用して行います。

クライアント入力を使って
権限判定をしてはいけません。

---

### hidden項目を信用しない

以下のようなコードがあります。

```html
<input type="hidden"
       name="price"
       value="1000">
```

利用者には見えませんが、
自由に変更可能です。

そのため、

```java
int price =
    Integer.parseInt(
        request.getParameter("price")
    );
```

のように
重要な情報をそのまま利用してはいけません。

---

### メソッド引数も検証する

入力値は画面入力だけではありません。

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

### assertによる検証を行わない

以下のコードは適切ではありません。

```java
assert user != null;
```

assertは実行環境によって
無効化される可能性があります。

入力値検証は通常のコードとして
実装してください。

---

### まとめ

入力値は信用しない。

特に、

- hidden項目
- URLパラメータ
- Cookie
- フォーム入力

を利用して
権限判定やセキュリティ判定を行ってはいけません。

また、

- メソッド引数は検証する
- assertによる検証は行わない

ことを徹底してください。

美しいコードとは、
安全で可読性の高いコードであると考えます。
