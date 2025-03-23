# local_agent
Agent that runs on local environment.

## Tech stack
LangChain, LangGraph and Ollama (qwen2.5:7b)

## Prerequisites
- Set up `.env`
- Install Ollama if necessary

## Usage
```
$ pipenv run agent
Loading .env environment variables...
Enter a message: 現在時刻は？
================================ Human Message =================================

現在時刻は？
================================== Ai Message ==================================
Tool Calls:
  current_datetime (e8d96b44-9114-43b7-a952-cbab541e3aa7)
 Call ID: e8d96b44-9114-43b7-a952-cbab541e3aa7
  Args:
================================= Tool Message =================================
Name: current_datetime

2025年03月23日 19:32:28
================================== Ai Message ==================================

現在の時刻は2025年03月23日 19:32:28です。
Enter a message: 先週金曜日の 日時は？
================================ Human Message =================================

先週金曜日時は？
================================== Ai Message ==================================

現在から先週の金曜日を計算しますと、2025年03月17日が先週の金曜日の日付となります。ただし、この回答はシステム時刻に基づいていますので、実際のシステム時刻が異なる場合はその差分をご了承ください。
Enter a message: 先週の金曜日の任天堂の株価は？
================================ Human Message =================================

先週の金曜日の任天堂の株価は？
================================== Ai Message ==================================
Tool Calls:
  tavily_search_results_json (91b8160d-03c9-406e-b764-f202052cb5f1)
 Call ID: 91b8160d-03c9-406e-b764-f202052cb5f1
  Args:
    query: 先週金曜日 任天堂 株価
================================= Tool Message =================================
Name: tavily_search_results_json

[{"title": "任天堂(株)【7974】：株価・株式情報 - Yahoo!ファイナンス", "url": "https://finance.yahoo.co.jp/quote/7974.T", "content": "取引値/前日比. 10,895. +345; +3.27%. 03/21 · 前日終値. 10,550. 03/19 · 始値. 10,750. 03/21 · 高値. 10,905. 03/21 · 安値. 10,675. 03/21 · 出来高. 6,406,700株. 03/21", "score": 0.7763013}, {"title": "任天堂【7974】の株価チャート - 株探", "url": "https://kabutan.jp/stock/chart?code=7974", "content": "7974 任天堂. 東証P 15:30. 10,895円. 前日比: +345", "score": 0.687468843}, {"title": "任天堂（7974）の株価推移 - 会社四季報オンライン", "url": "https://shikiho.toyokeizai.net/stocks/7974/timeline", "content": "前日終値. 10,285 (03/17). 任天堂のチャート. 概要 · 最新の四季報 · プロフィール · 四半期業績 · 長期業績; 株主優待; 株価推移 · 誌面アーカイブ.", "score": 0.55319832}]
================================== Ai Message ==================================

先週の金曜日（2025年3月17日）の任天堂の株価は、約10,550円でした。最新の取引価格は約10,895円で、前日比+345円、上昇率+3.27%となっています。

詳細なチャートや過去の業績情報については以下のリンクからご確認いただけます：
- [任天堂(株)【7974】：株価・株式情報 - Yahoo!ファイナンス](https://finance.yahoo.co.jp/quote/7974.T)
- [任天堂【7974】の株価チャート - 株探](https://kabutan.jp/stock/chart?code=7974)
- [任天堂（7974）の株価推移 - 会社四季報オンライン](https://shikiho.toyokeizai.net/stocks/7974/timeline)

```