# 組み込み関数
# Pythonのドキュメントに記載されている

import builtins

builtins.print('組み込み関数(例:ソート)')

ranking = {
    'A': 100,
    'B': 85,
    'C': 90
}

# ranking.get('A')

print(sorted(ranking, key=ranking.get, reverse=True))
