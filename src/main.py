import os
from riotwatcher import LolWatcher, RiotWatcher, ApiError

# api.jsonのパスを指定
api_path = os.path.join(os.path.dirname(__file__), '../api.json')

# api.jsonを読み取って表示
with open(api_path, 'r', encoding='utf-8') as f:
    api_key = f.read().strip()

# API周りの設定
lol_watcher = LolWatcher(api_key)
riot_watcher = RiotWatcher(api_key)

# LoL APIのregionとRiot APIのregionは異なる
lol_region = "jp1"
riot_region = "asia"

players = [
    {"name": "SHEILA", "tagline": "JP1"}
]

for player in players:
    # RiotWatcherのaccount.by_riot_idはregion, game_name, tagline
    my_account = riot_watcher.account.by_riot_id(
        region=riot_region,
        game_name=player['name'],
        tag_line=player['tagline']
    )

    me = lol_watcher.summoner.by_puuid(lol_region, my_account['puuid'])
    print(me)
    my_ranked_stats = lol_watcher.league.by_puuid(lol_region, me['puuid'])
    print(my_ranked_stats)