import pandas as pd

lol_stats = pd.read_csv("./lol_pro_stats_2020.csv")
# lol_stats["top_pick"] = ""
# lol_stats["jg_pick"] = ""
# lol_stats["mid_pick"] = ""
# lol_stats["bot_pick"] = ""
# lol_stats["sup_pick"] = ""
#
# for i in lol_stats.index:
#     if lol_stats["position"][i] == "team" and lol_stats["side"][i] == "Blue":
#         lol_stats["top_pick"][i+1] = lol_stats["champion"][i-10]
#         lol_stats["jg_pick"][i+1] = lol_stats["champion"][i-9]
#         lol_stats["mid_pick"][i+1] = lol_stats["champion"][i-8]
#         lol_stats["bot_pick"][i+1] = lol_stats["champion"][i-7]
#         lol_stats["sup_pick"][i+1] = lol_stats["champion"][i-6]

#     if lol_stats["position"][i] == "team" and lol_stats["side"][i] == "Red":
#         lol_stats["top_pick"][i+1] = lol_stats["champion"][i-6]
#         lol_stats["jg_pick"][i+1] = lol_stats["champion"][i-5]
#         lol_stats["mid_pick"][i+1] = lol_stats["champion"][i-4]
#         lol_stats["bot_pick"][i+1] = lol_stats["champion"][i-3]
#         lol_stats["sup_pick"][i+1] = lol_stats["champion"][i-2]


# lol_stats.to_csv("lol_pro_stats_2020.csv")
# print(data)
