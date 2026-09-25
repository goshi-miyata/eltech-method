# Copilotレビュー手順

## 1. テキスト生成

scripts/export_for_copilot.py を実行

生成物

export/eltech-method.txt

## 2. Copilotへ入力

入力内容

- export/eltech-method.txt
- レビューコメント

## 3. Copilot分析

以下を分析する

- 指摘は妥当か
- なぜそう読まれたか
- 修正すべきか
- 修正案

## 4. GitHub Issue登録

タイトル例

[Review][竹盛さん] 構造化・責務・テスト容易性の関係整理

## 5. Issue内容

- レビューコメント
- Copilot分析
- 議論内容
- 最終結論

を保存する

## 6. 修正

対象章を修正

## 7. Close

修正完了後にIssue Close
